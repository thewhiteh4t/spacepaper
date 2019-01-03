#!/usr/bin/env python

import os
import sys
import time
import signal
import random
import argparse
import requests
import datetime
import calendar
import threading
import subprocess as subp

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white

i = ''
key = ''
sv = ''
url = ''
arr = []
threads = []
version = '1.0.1'


os.system('clear')
# arguments
parser = argparse.ArgumentParser(
description='SpacePaper Provides High Quality Images from NASA APOD [ June 1995 Onwards ]')
parser.add_argument('-m', '--month', type=int, required=False, default = 7)
parser.add_argument('-y', '--year', type=int, required=False, default = 1996)
parser.add_argument('-r', '--random', required=False, action='store_true')
args = parser.parse_args()
Month = args.month
Year = args.year
Random = args.random

def banner():
	banner = r'''
   _____                       ____
  / ___/____  ____ _________  / __ \____ _____  ___  _____
  \__ \/ __ \/ __ `/ ___/ _ \/ /_/ / __ `/ __ \/ _ \/ ___/
 ___/ / /_/ / /_/ / /__/  __/ ____/ /_/ / /_/ /  __/ /
/____/ .___/\__,_/\___/\___/_/    \__,_/ .___/\___/_/
    /_/                               /_/'''
	print (G + banner + W + '\n')
	print (G + '[>]' + C + ' Created By : ' + W + 'thewhiteh4t')
	print (G + '[>]' + C + ' Version    : ' + W + version + '\n')

def updater():
	print (G + '[+]' + C + ' Checking For Updates...' + W, end='')
	update = requests.get('https://raw.githubusercontent.com/thewhiteh4t/spacepaper/master/version.txt', timeout = 5)
	update = update.text.split(' ')[1]
	update = update.strip()

	if update != version:
		print ('\n\n' + G + '[!]' + C + ' A New Version is Available : ' + W + update)
		ans = input('\n' + G + '[!]' + C + ' Update ? [y/n] : ' + W)
		if ans == 'y':
			print ('\n' + G + '[+]' + C + ' Updating...' + W + '\n')
			subp.check_output(['git', 'reset', '--hard', 'origin/master'])
			subp.check_output(['git', 'pull'])
			print ('\n' + G + '[+]' + C + ' Script Updated...Execute Again...' + W)
			sys.exit()
		elif ans == 'n':
			pass
		else:
			print ('\n' + R + '[-]' + C + ' Invalid Character...Skipping...'+ W)
	else:
		print (G + ' Up-to-date' + W)

def authkey():
	global key
	apikey = os.path.isfile('key.txt')
	if apikey == False:
		key = input('\n' + G + '[+]' + C + ' Enter API Key : ' + W)
		with open ('key.txt', 'w') as wkey:
			wkey.write(key)
		with open ('key.txt', 'r') as rkey:
			rdkey = rkey.read()
			rdkey = rdkey.replace('\n', '')
			key = rdkey
	else:
		with open ('key.txt', 'r') as rkey:
			rdkey = rkey.read()
			rdkey = rdkey.replace('\n', '')
			key = rdkey

def core():
	global Month, Year, Random, sv
	print (G + '[+]' + C + ' Starting PHP Server...' + W)
	print (G + '[+]' + C + ' URL : ' + W + 'http://127.0.0.1:8000/website')
	with open ('php.log', 'w') as log:
		sv = subp.Popen(['php', '-S', '127.0.0.1:8000/website'], stdout = log, stderr = log)

	if Random is True:
		rnd()
	elif not len(sys.argv) > 1: #check if no arg is passed
		default()
	else:
		mny()

def rnd():
	global Month, Year
	Month = 0
	Year = 0
	print (G + '[+]' + C + ' Random Mode...' + W)
	while True:
		Month = random.randint(1,12)
		Year = random.randint(1995,2019)
		master(i)
		input(G + '[+]' + C + ' Press Enter to Continue...' + W)

def default():
	global Month, Year
	while True:
		Month = int(input('\n' + G + '[+]' + C + ' Month : ' + W))
		Year = int(input(G + '[+]' + C + ' Year  : ' + W))
		print (G + '[+]' + C + ' Fetching Images from NASA APOD...' + W)
		master(i)

def mny():
	global Month, Year
	print (G + '[+]' + C + ' Fetching Images from NASA APOD...' + W)
	master(i)
	while True:
		Month = int(input('\n' + G + '[+]' + C + ' Month : ' + W))
		Year = int(input(G + '[+]' + C + ' Year  : ' + W))
		print (G + '[+]' + C + ' Fetching Images from NASA APOD...' + W)
		master(i)

def master(i):
	global total, Month, Year, url, arr
	total = calendar.monthrange(Year, Month)[1]
	print (G + '[+]' + C + ' Month/Year : ' + W + str(Month) + '/' + str(Year))
	for i in range(1,total+1):
		t = threading.Thread(target=gen, args=[i])
		t.daemon = True
		threads.append(t)
	for t in threads:
		try:
			t.start()
		except RuntimeError:
			pass
	for t in threads:
		t.join()
	img()
	print (G + '[+]' + C + ' SpacePaper is Ready...Reload Page...' + W)

def gen(i):
	global Year, Month, key, arr, url
	d = str(Year) + '-' + str(Month) + '-' + str(i)
	call = 'https://api.nasa.gov/planetary/apod?date={}&hd=True&api_key={}'.format(d, key)
	r = requests.get(call, headers={"content-type":"text"})
	if r.status_code == 200:
		dump = r.json()
		try:
			url = dump['hdurl']
			arr.append(url)
		except KeyError:
			try:
				url = dump['url']
				arr.append(url)
			except KeyError:
				print (G + '[!]' + C + ' Warning : ' + W + dump['msg'])
				exit()

def img():
	global url, arr
	with open ('website/js/spacepaper.js', 'w') as imgfile:
		imgfile.write(''' document.write(' ''')
		for link in arr:
			if 'youtube' in link:
				imgfile.write('<div class="grid-item">')
				imgfile.write('<iframe src="{}" width="250" frameborder="0" allow="gyroscope; picture-in-picture" allowfullscreen></iframe></div>'.format(link))
			else:
				imgfile.write('<div class="grid-item">')
				imgfile.write('<img src="{}"></div>'.format(link))
		imgfile.write(''' ') ''')
		arr = []
try:
	banner()
	updater()
	authkey()
	core()
except KeyboardInterrupt:
	print ('\n' + R + '[-]' + C + ' Keyboard Interrupt.' + W)
	os.kill(sv.pid, signal.SIGKILL)
