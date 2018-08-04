from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect

def global_data(view_func):
	def login_check(request,code=0):
		return view_func(request)
	return login_check