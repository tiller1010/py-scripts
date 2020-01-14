#!/usr/bin/env python

import sys

env = open('.env', 'w')

projectName = sys.argv[1];

env.write('# For a complete list of core environment variables see\n\
# https://docs.silverstripe.org/en/4/getting_started/environment_management/#core-environment-variables\n\
\n\
# DB credentials\n\
SS_DATABASE_CLASS="MySQLPDODatabase"\n\
SS_DATABASE_SERVER="localhost"\n\
SS_DATABASE_USERNAME="root"\n\
SS_DATABASE_PASSWORD=""\n\
SS_DATABASE_NAME="SS_{0}"\n\
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
CALENDAR_KEY=""'.format(projectName))

print('Generated .env for', projectName);

env.close()