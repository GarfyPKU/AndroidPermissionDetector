#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# simple tester: no train, on log output, no other functions, 
# only test an apk file simply.

# For market spider and website.

import os, argparse, datetime, json
from src import *

DIR_PATH = os.path.split(os.path.realpath(__file__))[0]
LOG_DIR_PATH = os.path.join(DIR_PATH, "log")
LOG_PATH = os.path.join(LOG_DIR_PATH, str(datetime.date.today())+".log")
PARAM_DIR_PATH = os.path.join(DIR_PATH, "param")
PARAM_DEFAULT_PATH = os.path.join(PARAM_DIR_PATH, "default")

def get_args():
	parser = argparse.ArgumentParser(
		description="Process args for Android Permission Tester")

	parser.add_argument('file',
						help='[Detect] The path of apk file to test')

	parser.add_argument('-V', '--version',
						action='version',
						version='Android Permission Tester 1.0.2')

	args = parser.parse_args()
	return args



def test(path):

	log.set_logger(filename=LOG_PATH, level="CRITICAL:DEBUG")

	if path:
		paramPath = PARAM_DEFAULT_PATH
		machineLearning = MachineLearning()
		result = machineLearning.test(path,paramPath)
		if result:
			log.info("Test finish.")
			log.info("result: "+str(result))
			return result
		else:
			log.error("You need an apk file to test.")
			log.error("Test abort")
			return

def commandLine():
	args = get_args()

	if not os.path.isdir(LOG_DIR_PATH):
		os.mkdir(LOG_DIR_PATH)
	log.set_logger(filename=LOG_PATH, level="CRITICAL:DEBUG")
	log.debug(str(args))

	score = float(test(args.file))

	if score:
		if score < 33.34:
			degree = "0"
		elif score < 66.67:
			degree = "1"
		elif score <= 100:
			degree = "2"
		else:
			degree = "unknown"

		result = {}
		result['score'] = score
		result['degree'] = degree

		print json.dumps(result)

if __name__ == "__main__":
	commandLine()