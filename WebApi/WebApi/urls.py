from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

from views import competitions
from views import organizations
#from ScoringEngine.ScoringEngine import urlsPlugins
#from ScoringEngine.ScoringEngine import urlsServices

urlpatterns = patterns('',
	#url(r'^competitions/(?P<competitionId>[0-9]+)/', include(urlsServices)),

	url(r'^competitions.json', competitions.competitions),
	url(r'^competitions/(?P<competitionId>[0-9]+).json', competitions.competition),
	url(r'^competitions/(?P<competitionId>[0-9]+)/teams.json', competitions.teams),
	url(r'^competitions/(?P<competitionId>[0-9]+)/teams/(?P<teamId>[0-9]+).json', competitions.team),
	url(r'^competitions/(?P<competitionId>[0-9]+)/scores.json', competitions.scores),
	url(r'^competitions/(?P<competitionId>[0-9]+)/scores/(?P<scoreId>[0-9]+).json', competitions.score),
	url(r'^competitions/(?P<competitionId>[0-9]+)/injects.json', competitions.injects),
	url(r'^competitions/(?P<competitionId>[0-9]+)/injects/(?P<injectId>[0-9]+).json', competitions.inject),
	url(r'^competitions/(?P<competitionId>[0-9]+)/injectresponses.json', competitions.injectresponses),
	url(r'^competitions/(?P<competitionId>[0-9]+)/injectresponses/(?P<injectResponseId>[0-9]+).json', competitions.injectresponse),
	url(r'^competitions/(?P<competitionId>[0-9]+)/incidents.json', competitions.incidents),
	url(r'^competitions/(?P<competitionId>[0-9]+)/incidents/(?P<incidentId>[0-9]+).json', competitions.incident),
	url(r'^competitions/(?P<competitionId>[0-9]+)/incidentresponses.json', competitions.incidentresponses),
	url(r'^competitions/(?P<competitionId>[0-9]+)/incidentresponses/(?P<incidentResponseId>[0-9]+).json', competitions.incidentresponse),

	url(r'^organizations.json', organizations.organizations),
	url(r'^organizations/(?P<organizationId>[0-9]+).json', organizations.organization),
	url(r'^organizations/(?P<organizationId>[0-9]+)/members.json', organizations.members),
	url(r'^organizations/(?P<organizationId>[0-9]+)/members/(?P<memberId>[0-9]+).json', organizations.member),
	url(r'^organizations/(?P<organizationId>[0-9]+)/competitions.json', organizations.competitions),
	url(r'^organizations/(?P<organizationId>[0-9]+)/competitions/(?P<competitionId>[0-9]+).json', organizations.competition),

	#url(r'^', include(urlsPlugins)),
	url(r'^users.json', organizations.users),
	url(r'^users/(?P<userId>[0-9]+).json', organizations.user)
)