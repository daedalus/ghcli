#!/usr/bin/env python
#
# Copyright Dario Clavijo 2015
# GPLv3 license

import json
import urllib2
import sys
import os

def fetch_json(url):
	response = urllib2.urlopen(url)
	if html := response.read():
		return json.loads(html)

def main():
	import argparse
	parser = argparse.ArgumentParser(description='github cloner')
	parser.add_argument('--username', dest='username', help='username')
	parser.add_argument('--clone-repos', dest='clonerepos', action='store_true', help='clone repos')
	parser.add_argument('--list-repos', dest='listrepos', action='store_true', help='list repos')
	parser.add_argument('--pull-repos', dest='pullrepos', action='store_true', help='list repos')

	args = parser.parse_args()
	user = args.username
	jsondata = fetch_json('https://api.github.com/users/%s/repos' % user)
	for i in xrange(len(jsondata)):
		repo_url = jsondata[i]['clone_url']
		description = jsondata[i]['description']
		name = jsondata[i]['name']
		if args.listrepos:
			print repo_url,description
		if args.clonerepos:
			os.system('git clone %s' % repo_url)
		if args.pullrepos:
			os.system('cd %s; git pull' % name)

if __name__ == "__main__":
	main()
