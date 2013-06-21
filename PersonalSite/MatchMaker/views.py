# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
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
		m = PotentialMatch.objects.create(name=request.POST['fullname'], gender=request.POST['gender'], MBTItype=request.POST['MBTI'], fbURL=request.POST['fb url'])
		myMatch = PotentialMatch.objects.get(MBTItype=matchDict[request.POST['MBTI']])
		myContext = {'name': myMatch.name, 'FbURL': myMatch.fbURL}
		return render(request, 'MatchResults.html', myContext)
   
