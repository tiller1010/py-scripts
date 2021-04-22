#!/usr/bin/env python

import sys
import re
from dotenv import load_dotenv
import os

load_dotenv()

hostsPath = os.getenv("HOSTS_PATH")
pyscriptsPath = os.getenv("PYSCRIPTS_PATH")

def insertAfter(filetext, regex, newText):
  """ Inserts 'newText' into 'filetext' right after 'regex'. """
  lastEntry = re.findall(regex, filetext)[-1]
  index = filetext.find(lastEntry)
  return filetext[:index + len(lastEntry)] + newText + filetext[index + len(lastEntry):]

if len(sys.argv) == 3:
	projectName = sys.argv[1];
	projectLocation = sys.argv[2];

	hosts = open(hostsPath, 'r+')
	hostsBackup = open(pyscriptsPath+'/hosts.txt', 'w+')

	hostsText = hosts.read()
	hostsBackup.write(hostsText)
	hostsBackup.close()

	if projectLocation == 'h' or projectLocation == 'homestead':
		print('Homestead project added to hosts file')
		hostsText = insertAfter(hostsText, r'192.168.10.10\s+[\w-]+.local', '\n192.168.10.10\t\t{0}.local'.format(projectName))
	elif projectLocation == 'x' or projectLocation == 'xampp':
		print('XAMPP project added to hosts file')
		hostsText = insertAfter(hostsText, r'127.0.0.1\s+[\w-]+.localhost', '\n127.0.0.1\t\t{0}.localhost'.format(projectName))
	else:
		print('Invalid project location, try "x" for xampp or "h" for homestead')
		sys.exit()

	hosts.seek(0)
	hosts.truncate()
	hosts.write(hostsText)
	hosts.close()
else:
	print('No project-type.')
	print('Try `hosts.py project-name x` for xampp')
	print('Try `hosts.py project-name h` for homestead')