#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Parse AndroidManifest.xml and Extract Permissions.

import xml.dom.minidom
import json

def _parse(dom, permissionPath=None):

	# get permission list
	root = dom.documentElement
	permissionList = []

	root = dom.documentElement
	permissionItems = root.getElementsByTagName('uses-permission')
	for permissionItem in permissionItems:
		permission = permissionItem.getAttribute('android:name')
		permissionList.append(permission)

	if permissionPath != None:
		try:
			f = open(permissionPath,"a")
			f.write(xmlPath+'\n'+json.dumps(permissionList)+'\n')
			f.close()
		except:
			"xmlParser.parseXml: write into json file error."
	return permissionList


def parseXml(xmlPath, permissionPath=None):
	print xmlPath+" parsing..."
	if xmlParser.endswith(".xml"):

		# parse AndroidManifest.xml
		try:
			dom = xml.dom.minidom.parse(xmlPath)
		except:
			print "xmlParser.parseXml: Parse error."
			return False
		return _parse(dom, permissionPath)
	else:
		print "xmlParser.parseXml: Unknown file type."
		return False

def parseString(xmlString):
	print "parsing..."
	try:
		dom = xml.dom.minidom.parseString(xmlString)
	except:
		print "xmlParser.parseString: Parse error."
		return False
	return _parse(dom)