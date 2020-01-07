#!/usr/bin/env python

import sys

# Update this file path if necessary
hosts = open('C:/Windows/System32/drivers/etc/hosts', 'r+')

projectType = sys.argv[1];
projectName = sys.argv[2];

# hosts.write('127.0.0.1\t{0}.localhost'.format(projectName))
if projectType == 'l' or projectType == 'laravel':
	print('it is a laravel project')
elif projectType == 's' or projectType == 'silverstripe':
	print('it is a silverstripe project')
else:
	print('Invalid project type, try "l" for laravel or "s" for silverstripe')

print(hosts.read().rfind('127.0.0.1'))

print('Generated hosts line for', projectName);

# def insertAfter(haystack, needle, newText):
#   """ Inserts 'newText' into 'haystack' right after 'needle'. """
#   i = haystack.find(needle)
#   return haystack[:i + len(needle)] + newText + haystack[i + len(needle):]