from django.conf import settings
from django.contrib.auth.models import check_password

from models import Team
from models import Admins

class TeamAuth(object):
	def authenticate(self, teamname=None, password=None, compid=None):
		try:
			print "teamname: '%s'" % teamname
			print "password: '%s'" % password
			print "compid: '%s'" % str(compid)
			team = Team.objects.get(teamname = teamname, password = password, compid = compid)
			return team
		except:
			return None

	def get_user(self, teamid):
		try:
			return Team.objects.get(teamid = teamid)
		except Team.DoesNotExist:
			return None

# class Admins(object):
# 	def authenticate():
# 		pass