competitionMin = {
	'name': 'New Competition',
	'url': 'new_competition',
	'organization': 1
}

competitionMax = {
	'organization': 1,
	'name': 'New Competition',
	'url': 'new_competition',
	'description': 'This is a description!',
	'datetimeDisplay': '',
	'datetimeStart': '',
	'datetimeFinish': '',
	'autoStart': True,
	'scoringEnabled': True,
	'scoringInterval': 90,
	'scoringIntervalUncertainty': 20,
	'scoringMethod': 'fqdn',
	'scoringSlaEnabled': True,
	'scoringSlaPenalty': 50,
	'servicesEnabled': True,
	'teamsViewRankingEnabled': True,
	'teamsViewScoreboardEnabled': True,
	'teamsViewServiceStatisticsEnabled': True,
	'teamsViewServiceStatusEnabled': True,
	'teamsViewIncidentResponseEnabled': True
}

team = {
	"competitionId": 1,
	"name": "Team Name",
	"username": "teamname",
	"password": "password",
	"networkCidr": "192.168.1.0/24",
	"scorConfigurations": "{}"
}

score = {
	'competitionId': 1,
	'teamId': 1,
	'serviceId': 1,
	'datetime': "2015-07-15 20:30:15",
	'value': 10,
	'message': "Test Subject"
}

inject = {
	'competitionId': 1,
	'requireResponse': True,
	'manualDelivery': False,
	'datetimeDelivery': "",
	'datetimeResponseDue': "",
	'datetimeResponseClose': "",
	'title': "Test Title",
	'body': "Contents of inject description"
}

injectResponse = {
	'competitionId': 1,
	'teamId': 1,
	'injectId': 1,
	'datetime': "2015-07-15 20:30:15",
	'content': "test content",
}

incident = {
	'competitionId': 1,
	'teamId': 1,
	'datetime': "2015-07-15 20:30:15",
	'subject': "Test Subject",
	'content': "test content",	
}

incidentResponse = {
	'competitionId': 1,
	'teamId': 1,
	'replyTo': 0,
	'datetime': "2015-07-15 20:30:15",
	'subject': "Test Subject",
	'content': "test content"
}

organization = {
	'name': "New Organization",
	'deleteable': False,
	'url': "new_organization",
	'description': "This is a short description!",
	'maxMembers': 5,
	'maxCompetitions': 5,
}

user = {
	'name': "Test User",
	'password': "password",
	'organizationId': 1
}

document = {
	'inject': None,
	'injectResponse': None,
	'incidentResponse': None,
	'plugin': 1,
	'contentType': "text/plain",
	'fileHash': "87deb342e0ded1377271fc307601f0bc",
	'filePath': "testfile.txt",
	'filename': "testfile.txt",
	'urlEncodedFilename': "testfile.txt"
}
