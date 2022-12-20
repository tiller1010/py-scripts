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
		env = open('.env', 'w')
		env.write('APP_NAME=Laravel\n\
APP_ENV=local\n\
APP_KEY=\n\
APP_DEBUG=true\n\
APP_URL=http://{0}.local\n\
\n\
LOG_CHANNEL=stack\n\
\n\
DB_CONNECTION=mysql\n\
DB_HOST=127.0.0.1\n\
DB_PORT=3306\n\
DB_DATABASE=LV_{0}\n\
DB_USERNAME={1}\n\
DB_PASSWORD={2}\n\
\n\
BROADCAST_DRIVER=log\n\
CACHE_DRIVER=file\n\
QUEUE_CONNECTION=sync\n\
SESSION_DRIVER=file\n\
SESSION_LIFETIME=120\n\
\n\
REDIS_HOST=127.0.0.1\n\
REDIS_PASSWORD=null\n\
REDIS_PORT=6379\n\
\n\
MAIL_DRIVER=smtp\n\
MAIL_HOST=smtp.mailtrap.io\n\
MAIL_PORT=2525\n\
MAIL_USERNAME=null\n\
MAIL_PASSWORD=null\n\
MAIL_ENCRYPTION=null\n\
\n\
AWS_ACCESS_KEY_ID=\n\
AWS_SECRET_ACCESS_KEY=\n\
AWS_DEFAULT_REGION=us-east-1\n\
AWS_BUCKET=\n\
\n\
PUSHER_APP_ID=\n\
PUSHER_APP_KEY=\n\
PUSHER_APP_SECRET=\n\
PUSHER_APP_CLUSTER=mt1\n\
\n\
MIX_PUSHER_APP_KEY=\n\
MIX_PUSHER_APP_CLUSTER=\n\
\n\
SCOUT_DRIVER=tntsearch'.format(projectName, databaseUser, databasePassword))

	elif projectType == 'w' or projectType == 'wordpress':
		env = open('.env', 'w')
		env.write('DB_NAME=WP_{0}\n\
DB_USER={1}\n\
DB_PASSWORD={2}\n\
DB_HOST=localhost'.format(projectName, databaseUser, databasePassword))

	else:
		env = open('.env', 'w')
		env.write('# For a complete list of core environment variables see\n\
# https://docs.silverstripe.org/en/4/getting_started/environment_management/#core-environment-variables\n\
\n\
# DB credentials\n\
SS_DATABASE_CLASS="MySQLPDODatabase"\n\
SS_DATABASE_SERVER="localhost"\n\
SS_DATABASE_USERNAME="{1}"\n\
SS_DATABASE_PASSWORD="{2}"\n\
SS_DATABASE_NAME="SS_{0}"\n\
\n\
# Development - Should be turned off for production\n\
SS_ENVIRONMENT_TYPE="dev"\n\
SS_DEFAULT_ADMIN_USERNAME="admin"\n\
SS_DEFAULT_ADMIN_PASSWORD="password"\n\
\n\
# The active theme\n\
SS_THEME="{0}"\n\
\n\
# SilverStripe TOTP Authenticator - Update to a string related to site\n\
SS_MFA_SECRET_KEY="silverstripe-{0}"\n\
\n\
# Calendar Settings\n\
CALENDAR_SHARED=false\n\
CALENDAR_TZ="America/New_York"\n\
CALENDAR_URL=""\n\
CALENDAR_KEY=""'.format(projectName, databaseUser, databasePassword))

	print('Generated .env for', projectName);
	print('Try `env.py project-type project-name x` for xampp')

	env.close()
else:
	print('No project-type.')
	print('Try `env.py s project-name` for silverstripe')
	print('Try `env.py l project-name` for laravel')
	print('Try `env.py project-type project-name x` for xampp')