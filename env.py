#!/usr/bin/env python

import sys

env = open('.env', 'w')

projectName = sys.argv[1];

env.write('# For a complete list of core environment variables see\n# https://docs.silverstripe.org/en/4/getting_started/environment_management/#core-environment-variables\n\n# DB credentials\nSS_DATABASE_CLASS="MySQLPDODatabase"\nSS_DATABASE_SERVER="localhost"\nSS_DATABASE_USERNAME="root"\nSS_DATABASE_PASSWORD=""\nSS_DATABASE_NAME="SS_{0}"\n\n# Development - Should be turned off for production\nSS_ENVIRONMENT_TYPE="dev"\nSS_DEFAULT_ADMIN_USERNAME="admin"\nSS_DEFAULT_ADMIN_PASSWORD="password"\n\n# SilverStripe TOTP Authenticator - Update to a string related to site\nSS_MFA_SECRET_KEY="silverstripe-install"'.format(projectName))

print('Generated .env for', projectName);

env.close()