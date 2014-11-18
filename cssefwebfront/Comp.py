from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from models import Competition
from models import Service
from models import Inject
from models import Score
from models import Team
from forms import TeamLoginForm


from django.contrib.auth import authenticate

class UserMessages:
	def __init__(self):
		self.info = []
		self.error = []
		self.success = []
	def new_info(self, string, num):
		self.info.append({"string":string, "num":num})

	def new_error(self, string, num):
		self.error.append({"string":string, "num":num})

	def new_success(self, string, num):
		self.success.append({"string":string, "num":num})

	def clear(self):
		self.info = []
		self.error = []
		self.success = []

def login(request, competition = None):
	"""
	Page for teams to login to for a competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["form"] = {'login': TeamLoginForm()}
	c["competition_object"] = Competition.objects.get(compurl = competition)
	c.update(csrf(request))
	# Checks if the user is submitting the form, or requesting the form
	if request.method != "POST":
		return render_to_response('Comp/login.html', c)

	form_dict = request.POST.copy()
	form_dict["compid"] = c["competition_object"].compid

	team = authenticate(teamname = form_dict["teamname"], password = form_dict["password"], compid = form_dict["compid"])
	if team == None:
		c["messages"].new_info("Incorrect team credentials.", 4321)
		return render_to_response('Comp/login.html', c)
	auth.login(request, team)
	return HttpResponseRedirect("/competitions/%s/summary/" % competition)

def logout(request, competition = None):
	"""
	Page for teams to logout of a competition
	"""
	auth.logout(request)
	c = {}
	c["messages"] = UserMessages()
	return HttpResponseRedirect("/competitions/%s/summary/" % competition)

def list(request):
	"""
	Display list of competitions
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_list"] = Competition.objects.all()
	return render_to_response('Comp/list.html', c)

def summary(request, competition = None):
	"""
	Display summary information for selected competition
	"""
	current_url = request.build_absolute_uri()
	if request.build_absolute_uri()[-8:] != "summary/":
		return HttpResponseRedirect(current_url + "summary/")
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if request.user.is_authenticated():
		c["team_auth"] = True
	else:
		c["team_auth"] = False

	return render_to_response('Comp/summary.html', c)

def details(request, competition = None):
	"""
	Display details about the selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	c["services"] = Service.objects.filter(compid = c["competition_object"].compid)
	c["teams"] = Team.objects.filter(compid = c["competition_object"].compid)
	if request.user.is_authenticated():
		c["team_auth"] = True
	else:
		c["team_auth"] = False
	return render_to_response('Comp/details.html', c)

def rankings(request, competition = None):
	"""
	Display team rankings for selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	c["ranks"] = []
	team_objs = Team.objects.filter(compid = c["competition_object"].compid)
	for i in team_objs:
		scores_objs = Score.objects.filter(compid = c["competition_object"].compid, teamid=i.teamid)
		total = 0
		for k in scores_objs:
			total += k.value
		c["ranks"].append({"team": i.teamname, "score": total, "place":0})
	if request.user.is_authenticated():
		c["team_auth"] = True
	else:
		c["team_auth"] = False		
	return render_to_response('Comp/rankings.html', c)

def injects(request, competition = None):
	"""
	Display inject list for selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if not request.user.is_authenticated():
		c["team_auth"] = False
		return render_to_response('Comp/injects.html', c)
	c["team_auth"] = True
	c["injects"] = Inject.objects.filter(compid = c["competition_object"].compid)
	return render_to_response('Comp/injects.html', c)

def servicestatus(request, competition = None):
	"""
	Display current service status for selected team in selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if not request.user.is_authenticated():
		c["team_auth"] = False
		return render_to_response('Comp/servicestatus.html', c)
	c["team_auth"] = True
	return render_to_response('Comp/servicestatus.html', c)

def servicetimeline(request, competition = None):
	"""
	Display status timeline of services for selected team in selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if not request.user.is_authenticated():
		c["team_auth"] = False
		return render_to_response('Comp/servicetimeline.html', c)
	c["team_auth"] = True
	return render_to_response('Comp/servicetimeline.html', c)

def scoreboard(request, competition = None):
	"""
	Display the list of scores for the selected team of the selected competition
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if not request.user.is_authenticated():
		c["team_auth"] = False
		return render_to_response('Comp/scoreboard.html', c)
	c["team_auth"] = True
	c["scores"] = Score.objects.filter(compid = c["competition_object"].compid, teamid = request.user.teamid)
	# score_obj_list = Score.objects.filter(compid = c["competition_object"].compid, teamid = request.user.teamid)
	# for i in score_obj_list:
	# 	score_obj_dict = {}
	# 	score_obj_dict["time"] = i.datetime
	# 	score_obj_dict["name"] = Service.objects.get(servid = i.servid).name
	# 	score_obj_dict["value"] = i.value
	# 	score_list.append(score_obj_dict)
	return render_to_response('Comp/scoreboard.html', c)

def incidentresponse(request, competition = None):
	"""
	Provides a submission portal for selected team of selected competition to submit incident responses
	"""
	c = {}
	c["messages"] = UserMessages()
	c["competition_object"] = Competition.objects.get(compurl = competition)
	if not request.user.is_authenticated():
		c["team_auth"] = False
		return render_to_response('Comp/incidentresponse.html', c)
	c["team_auth"] = True
	return render_to_response('Comp/incidentresponse.html', c)
