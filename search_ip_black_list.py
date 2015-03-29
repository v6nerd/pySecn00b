#!/usr/bin/python
import sys
import re
import urllib2
import httplib
import ipaddr as ip
import os
from termcolor import colored

list=(sys.path[0] + '/ip_black_list')

def cache_check():
	#list=(sys.path[0] + '/ip_black_list')
	if os.path.exists(list):
		ip_cache=file(list, 'r').readlines()
		return ip_cache
	else:
	    list_construct()

if len(sys.argv)!=2:
	print "Usage: python search_ip_BlackList.py <ip address>"
	#print sys.path[0]
	sys.exit(0)
	
ip_pattern=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
#ip_coll=0

url_list=[
'https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist',
'https://spyeyetracker.abuse.ch/blocklist.php?download=ipblocklist',
'http://www.openbl.org/lists/base.txt',
'https://palevotracker.abuse.ch/blocklists.php?download=ipblocklist',
'http://malc0de.com/bl/IP_Blacklist.txt',
'http://rules.emergingthreats.net/blockrules/compromised-ips.txt',
'http://www.malwaredomainlist.com/hostslist/ip.txt',
'http://www.ciarmy.com/list/ci-badguys.txt',
'https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.csv',
'http://support.clean-mx.de/clean-mx/xmlviruses.php',
'http://www.projecthoneypot.org/list_of_ips.php?rss=1&rf=40809'
]

def ip_check(ip_query):
	try:
	 if ip.IPv4Address(ip_query):
		return ip_query
	except ip.AddressValueError as error:
		print str(error) + " is invalid"
		sys.exit(0)

def list_construct():
	items=""
	for url in url_list:
		try:
	  	 url_connect=urllib2.urlopen(url)
	  	 ip_blocks=url_connect.read()
	  	 ip_list=(re.findall(ip_pattern, ip_blocks))
		 items = str(ip_list) + items
		except urllib2.URLError as error:
			print error.reason
		except urllib2.HTTPError as error:
			print error.reason
		except httplib.BadStatusLine as error:
			print error
	#return ip_list
	#print ip_list
	return items
	cache_write(items)

def cache_write(items):
	with file('ip_blacklist', 'w') as out_file:
		out_file.write(items) 

def ip_search(list):
	ip_coll=0
	listed_ip=""
	for block_list in list:
		ip_coll +=len(block_list)
		if ip_addr in block_list:
			listed_ip+=ip_addr
			print "IP:" + colored(str(listed_ip), 'red') + " Found"
	print "TOTAL IP Addresses Queried:" + str(ip_coll)


ip_addr=(ip_check(sys.argv[1]))
cache_check()

#list_construct()
#list_refine(ip_list)
#ip_search(ip_list)
