from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
	if 'msg' in request.GET:
		msg = request.GET['msg']
		r = requests.get(" http://www.hanmoto.com/api/book.php?ISBN=" + msg)
		result = r.text
		sresult ='you typed:"' + msg + '".'
	else:
		result = 'please send msg parameter!'
	return HttpResponse(result)