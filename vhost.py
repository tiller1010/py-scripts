#!/usr/bin/env python

import sys

# Update this file path if necessary
vhost = open('C:/xampp/apache/conf/extra/httpd-vhosts.conf', 'a')

projectName = sys.argv[1];

# Change to your email
vhost.write('\n\
<VirtualHost *:80>\n\
\tServerAdmin tyler@werkbot.com\n\
\tDocumentRoot "C:/xampp/htdocs/{0}/public"\n\
\tServerName {0}.localhost\n\
\tErrorLog "logs/{0}-error.log"\n\
\tCustomLog "logs/{0}-access.log" common\n\
</VirtualHost>\n\
'.format(projectName))

print('Generated vhost block for', projectName);

vhost.close()