#!/usr/bin/env python

import sys
import re

def insertAfter(filetext, regex, newText):
  """ Inserts 'newText' into 'filetext' right after 'regex'. """
  lastEntry = re.findall(regex, filetext)[-1]
  index = filetext.find(lastEntry)
  return filetext[:index + len(lastEntry)] + newText + filetext[index + len(lastEntry):]

# Update this file path if necessary
hosts = open('C:/Windows/System32/drivers/etc/hosts', 'r+')

projectType = sys.argv[1];
projectName = sys.argv[2];

hostsText = hosts.read()

# hosts.write('127.0.0.1\t{0}.localhost'.format(projectName))
if projectType == 'l' or projectType == 'laravel':
	print('Laravel project added to hosts file')
	hostsText = insertAfter(hostsText, r'192.168.10.10\s+[\w-]+.localhost', '\n192.168.10.10\t{0}.localhost'.format(projectName))
elif projectType == 's' or projectType == 'silverstripe':
	print('Silverstripe project added to hosts file')
	hostsText = insertAfter(hostsText, r'127.0.0.1\s+[\w-]+.localhost', '\n127.0.0.1\t\t{0}.localhost'.format(projectName))
else:
	print('Invalid project type, try "l" for laravel or "s" for silverstripe')
	sys.exit()

hosts.seek(0)
hosts.truncate()
hosts.write(hostsText)