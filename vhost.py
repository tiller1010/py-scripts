#!/usr/bin/env python

import sys
from dotenv import load_dotenv
import os

load_dotenv()

vhostPath = os.getenv("VHOST_PATH")
email = os.getenv("EMAIL")

vhost = open(vhostPath, 'a')

projectName = sys.argv[1];

vhost.write('\n\
<VirtualHost *:80>\n\
\tServerAdmin {1}\n\
\tDocumentRoot "C:/xampp/htdocs/{0}/public"\n\
\tServerName {0}.localhost\n\
\tErrorLog "logs/{0}-error.log"\n\
\tCustomLog "logs/{0}-access.log" common\n\
</VirtualHost>\n\
'.format(projectName, email))

print('Generated vhost block for', projectName);

vhost.close()