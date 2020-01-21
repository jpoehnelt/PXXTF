#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

from lib import wphttp
from lib import wpprint

class wprobots:
	
	chk = wphttp.UCheck() 
	out = wpprint.wpprint()
	
	def __init__(self,agent,proxy,redir,time,url,cookie):
		self.url = url
		self.cookie = cookie
		self.req = wphttp.wphttp(
			agent=agent,proxy=proxy,
			redir=redir,time=time
			)
	def run(self):
		try:
			url = wprobots.chk.path(self.url,'/robots.txt')
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp._content != None:
				if resp.url == url:
					wprobots.out.plus('Robots available under: {}'.format(resp.url))
					print "-------------------------\r\n{}\n-------------------------".format(resp._content)
		except Exception,e:
			pass