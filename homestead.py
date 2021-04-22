#!/usr/bin/env python

import sys
import re
from dotenv import load_dotenv
import os

load_dotenv()

homesteadPath = os.getenv("HOMESTEAD_PATH")
silverstripePath = os.getenv("SILVERSTRIPE_SITES_PATH")
laravelPath = os.getenv("LARAVEL_APPS_PATH")
pyscriptsPath = os.getenv("PYSCRIPTS_PATH")

def insertAfter(filetext, regex, newText):
  """ Inserts 'newText' into 'filetext' right after 'regex'. """
  lastEntry = re.findall(regex, filetext)[-1]
  # print(lastEntry)
  index = filetext.find(lastEntry)
  return filetext[:index + len(lastEntry)] + newText + filetext[index + len(lastEntry):]

if len(sys.argv) == 3:
	projectType = sys.argv[1];
	projectName = sys.argv[2];

	homestead = open(homesteadPath, 'r+')
	homesteadBackup = open(pyscriptsPath+'/homestead.txt', 'w+')

	homesteadText = homestead.read()
	homesteadBackup.write(homesteadText)
	homesteadBackup.close()

	# Need to update this to include env setting for paths
	if projectType == 'l' or projectType == 'laravel':
		print('Laravel project added to homestead file')
		homesteadText = insertAfter(homesteadText, r'to: /home/vagrant/[\w-]+', '\n    - map: {0}/{1}\n      to: /home/vagrant/{1}'.format(laravelPath, projectName))
		homesteadText = insertAfter(homesteadText, r'/home/vagrant/[\w-]+/public\s+php: .+', '\n    - map: {0}.local\n      to: /home/vagrant/{0}/public\n      php: \'7.3\''.format(projectName))
		homesteadText = insertAfter(homesteadText, r'LV_[\w-]+', '\n    - LV_{0}'.format(projectName))
	elif projectType == 's' or projectType == 'silverstripe':
		print('Silverstripe project added to homestead file')
		homesteadText = insertAfter(homesteadText, r'to: /home/vagrant/[\w-]+', '\n    - map: {0}/{1}\n      to: /home/vagrant/{1}'.format(silverstripePath, projectName))
		homesteadText = insertAfter(homesteadText, r'/home/vagrant/[\w-]+/public\s+php: .+', '\n    - map: {0}.local\n      to: /home/vagrant/{0}/public\n      php: \'7.3\''.format(projectName))
		homesteadText = insertAfter(homesteadText, r'SS_[\w-]+', '\n    - SS_{0}'.format(projectName))
	else:
		print('Invalid project type, try "l" for laravel or "s" for silverstripe')
		sys.exit()

	homestead.seek(0)
	homestead.truncate()
	homestead.write(homesteadText)
	homestead.close()
else:
	print('No project type.')
	print('Try `homestead.py s project-name` for silverstripe')
	print('Try `homestead.py l project-name` for laravel')