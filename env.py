#!/usr/bin/env python

import sys



if len(sys.argv) == 4:
	projectLocation = sys.argv[3];
	if projectLocation == 'x' or projectLocation == 'xampp':
		databaseUser = 'root'
		databasePassword = ''
	else:
		databaseUser = 'homestead'
		databasePassword = 'secret'
else:
	databaseUser = 'homestead'
	databasePassword = 'secret'

if len(sys.argv) >= 3:
	projectType = sys.argv[1];
	projectName = sys.argv[2];

	if projectType == 'l' or projectType == 'laravel':
		databaseType = 'LV'
	else:
		databaseType = 'SS'


	env = open('.env', 'w')
	env.write('# For a complete list of core environment variables see\n\
# https://docs.silverstripe.org/en/4/getting_started/environment_management/#core-environment-variables\n\
\n\
# DB credentials\n\
SS_DATABASE_CLASS="MySQLPDODatabase"\n\
SS_DATABASE_SERVER="localhost"\n\
SS_DATABASE_USERNAME="{1}"\n\
SS_DATABASE_PASSWORD="{2}"\n\
SS_DATABASE_NAME="{3}_{0}"\n\
\n\
# Development - Should be turned off for production\n\
SS_ENVIRONMENT_TYPE="dev"\n\
SS_DEFAULT_ADMIN_USERNAME="admin"\n\
SS_DEFAULT_ADMIN_PASSWORD="password"\n\
\n\
# SilverStripe TOTP Authenticator - Update to a string related to site\n\
SS_MFA_SECRET_KEY="silverstripe-{0}"\n\
\n\
# Calendar Settings\n\
CALENDAR_SHARED=false\n\
CALENDAR_TZ="America/New_York"\n\
CALENDAR_URL=""\n\
CALENDAR_KEY=""'.format(projectName, databaseUser, databasePassword, databaseType))

	print('Generated .env for', projectName);
	print('Try `env.py project-type project-name x` for xampp')

	env.close()
else:
	print('No project-type.')
	print('Try `env.py s project-name` for silverstripe')
	print('Try `env.py l project-name` for laravel')
	print('Try `env.py project-type project-name x` for xampp')