#!/usr/bin/env python

import sys
import os
from dotenv import load_dotenv
import os
import re
import webbrowser

load_dotenv()

def viewProject():
	# If viewing a project
	missingProjectURL = True
	projectEnv = open('.env', 'r')
	with projectEnv as file:
		for line in file:
			if 'TEAMWORK_PROJECT_URL' in line:
				url = re.sub(r'TEAMWORK_PROJECT_URL=|"', '', line)
				print('Opening project at:', url)
				webbrowser.open(url)
				missingProjectURL = False
				break

	if missingProjectURL:
		print('Missing TEAMWORK_PROJECT_URL in .env')

	projectEnv.close()

# If viewing a task
if len(sys.argv) == 2:
	option = sys.argv[1]
	if(option == 't' or option == 'task'):
		missingTaskURL = True
		teamworkDomain = os.getenv('TEAMWORK_DOMAIN')
		pullRequest = os.popen('gh pr view')
		with pullRequest as output:
			for line in output:
				if teamworkDomain in line:
					print('Opening task at:', line)
					webbrowser.open(line)
					missingTaskURL = False
					break

		if missingTaskURL:
			print('Missing task URL in pull request')
	else:
		viewProject()
else:
	viewProject()