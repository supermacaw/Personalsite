# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from MatchMaker import models

def home_page(request):
	return render(request, 'DatingApp.html', {}) 

def make_match(request):
	if request.method == 'POST':
		m = PotentialMatch.objects.create(name=request.POST['fullname'], gender=request.POST['gender'], MBTItype=request.POST['MBTI'], fbURL=request.POST['fb url'])
    
