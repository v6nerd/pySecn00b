import sys
import smtplib
import getpass
from time import sleep
from time import strftime
from email.mime.text import MIMEText

def main():
	if len(sys.argv)!=3:
		print'''
==================================
Arcsight Notfication Trace Utility
==================================

Usage: %s <log file> [OPTION]
-w trace WARN flags
-e trace ERROR flags
-a trace ALL (Warnings & Errors)
''' % sys.argv[0]
		sys.exit(0)

	else:
		inFile=open(sys.argv[1],'r').readlines()
		cflag=sys.argv[2]
		file=open(sys.argv[1],'r')
		smtp_connect('smtp.gmail.com',587)
		if cflag=='-w':
			trace_warn(file)
		if cflag=='-e':
			trace_error(file)
		if cflag=='-a':
			trace_all(file)

def trace_warn(input):
	while True:
		line=str(tail_read(input))
		if "WARN" in line:
			mail_notify(line.strip('\n'),'WARNING')
	
def trace_error(input):
	while True:
		line=str(tail_read(input))
                if "ERROR" in line: 
			mail_notify(line.strip('\n'),'ERROR')


def trace_all(input):
	while True:
		line=str(tail_read(input))
		if "WARN" in line or "ERROR" in line:
			mail_notify(line.strip('\n'),"ALL")

def mail_notify(input,type):
	sender='user@mail.com'
	receiver='user@mail.com'
	message=MIMEText(input)
	message['From']=sender
	message['To']=receiver
	message['Subject']='Arcsight Event Notification - %s' % type
	
	try:
         print '%s Sending Notification %s' % (strftime('%y-%m-%d|%H:%M:%S'),type)
	 mail_server.sendmail(sender,receiver,message.as_string())
	except smtplib.SMTPException:
	 raise

def tail_read(inputFile):
	line=inputFile.readline()
	if line:
		return line
	else:
		tail(inputFile)

def tail(inputFile):
	s_interval=2.0
	last_line=inputFile.tell()
	line=inputFile.readline()
	if not line:
		sleep(s_interval)
		return inputFile.seek(last_line)
			
	else:
		return line

def smtp_connect(server,port):
	user_id='user@mail.com'
	passwd=getpass.getpass()
	if passwd:
	 print 'Trying to Authenticate...'
	 try:
	   global mail_server
           mail_server=smtplib.SMTP(server,port)
           mail_server.ehlo()
           mail_server.starttls()
           mail_server.ehlo()
           mail_server.login(user_id,passwd)
	   print 'Authentication Succeded!\n'	
	   return mail_server
         except smtplib.SMTPException, smtplib.SMTPAuthenticationError:
           raise


if __name__ == '__main__':
	main()
