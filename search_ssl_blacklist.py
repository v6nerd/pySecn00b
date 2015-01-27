#!/bin/python

import sys
import re
import feedparser

def sslbl_parse():

	sslbl_feed="https://sslbl.abuse.ch/sslbl.rss"
	sslbl_parse=feedparser.parse(sslbl_feed)
	sslbl_sha=""

	for item in sslbl_parse.entries:
		sslbl_entries=(item.description).split(",")
		sslbl_sha+=re.sub(r'^(.*) ',"",sslbl_entries[0]))
	print sslbl_sha

sslbl_parse()
