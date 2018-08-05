import time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from .forms import *
from django.views import View

from .models import *
# Create your views here.

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.backend import clear_session

import schedule
import time

import pyscreenshot as ImageGrab
continuous_monitoring=0

from .decorators import global_data

@global_data
def test(request):
	data={}
	return HttpResponse("Working")

@global_data
def home(request):
	if 'continuous_monitoring' not in request.session:
		request.session['continuous_monitoring']=0
	print(request.session['continuous_monitoring'])
	data={}
	data['continuous_monitoring']=request.session['continuous_monitoring']
	return render(request,'main/home.html',data)

class upload(View):
	def get(self, request):
		if 'continuous_monitoring' not in request.session:
			request.session['continuous_monitoring']=0
		data={}
		data['continuous_monitoring']=request.session['continuous_monitoring']
		photos_list = Photo.objects.all()
		data['photos']=photos_list
		return render(self.request, 'main/upload.html', data)

	def post(self, request):
		form = PhotoForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			photo = form.save()
			data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
		else:
			data = {'is_valid': False}
		return JsonResponse(data)

@global_data
def check(request):
	test_datagen = ImageDataGenerator(rescale = 1./255)
	classifier = load_model('main/save_data.h5')
	result_set = test_datagen.flow_from_directory('main/photos/',target_size = (64, 64),batch_size = 32,class_mode = 'binary',shuffle=False)
	result = classifier.predict_generator(result_set,workers=1)
	al_result_fname=Result.objects.all().values_list('file_name',flat=True)
	for i in range(len(result_set.filenames)):
		print(result_set.filenames[i],result[i])
		fname=result_set.filenames[i]
		prob=result[i]
		if fname not in al_result_fname:
			obj=Result()
			obj.file_name=fname
			obj.file_url=fname
			obj.percentage_safe=(1-prob)*100
			obj.save()

	clear_session()

	del result
	del result_set
	del classifier
	del test_datagen
	return redirect('/photo/result')

@global_data
def result(request):
	if 'continuous_monitoring' not in request.session:
		request.session['continuous_monitoring']=0
	data={}
	data['continuous_monitoring']=request.session['continuous_monitoring']
	all_obj=Result.objects.all()
	data['all_obj']=all_obj
	return render(request,'main/result.html',data)

@global_data
def continuous(request):
	request.session['continuous_monitoring']=1
	request.session.save()
	print(request.session['continuous_monitoring'])
	print("continuous")
	data={}
	def job():
		print("Monitoring")
		im=ImageGrab.grab()
		im.save("main/screenshot/nsfw/screengrab.jpeg", "JPEG")
		test_datagen = ImageDataGenerator(rescale = 1./255)
		classifier = load_model('main/save_data.h5')
		result_set = test_datagen.flow_from_directory('main/screenshot/',target_size = (64, 64),batch_size = 32,class_mode = 'binary',shuffle=False)
		result = classifier.predict_generator(result_set,workers=1)
		clear_session()
		print(result)
	schedule.every(1).seconds.do(job).tag('job', 'task')

	while True:
		schedule.run_pending()

@global_data
def continuous_off(request):	
	data={}
	request.session['continuous_monitoring']=0
	request.session.save()
	print(request.session['continuous_monitoring'])
	try:
		schedule.clear('job')
	except:
		pass
	return redirect('/photo/home')

@global_data
def delete_all_photos(request):
	all_photos=Photo.objects.all()
	for photo in all_photos:
		photo.file.delete()
		photo.delete()

	all_result=Result.objects.all()
	all_result.delete()
	return redirect('/photo/upload')