# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
from MatchMaker import models

matchDict = dict(ESTJ='ISTP', ISTP='ESTJ')
							# ESTP=[],
							# ESFJ=[],
							# ESFP=[],
							# ENTJ=[]
							# ENTP=[],
							# ENFJ=[],
							# ENFP=[],
							# ISTJ=[],
							# ISTP='ESTJ',
							# ISFJ=[],
							# ISFP=[],
							# INTJ=[],
							# INTP=[],
							# INFJ=[],
							# INFP=[]
							#)

def home_page(request):
	return render(request, 'DatingApp.html', {}) 

def create_and_match(request):
	if request.method == 'POST':
		m = models.PotentialMatch.objects.create(name=request.POST['fullname'], gender=request.POST['gender'], MBTItype=request.POST['MBTI'], fbURL=request.POST['fb url'])
		myMatch = models.PotentialMatch.objects.filter(MBTItype=matchDict[request.POST['MBTI']])
		if len(myMatch) > 0:
			myContext = {'name': myMatch[0].name, 'FbURL': myMatch[0].fbURL}
			return render(request, 'MatchResults.html', myContext)
   		else:
   			return render(request, 'DatingApp.html', {})
