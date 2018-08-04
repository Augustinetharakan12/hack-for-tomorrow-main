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



def test(request):
	return HttpResponse("Working")

def home(request):
	data={}
	return render(request,'main/home.html',data)

class upload(View):
	def get(self, request):
		photos_list = Photo.objects.all()
		return render(self.request, 'main/upload.html', {'photos': photos_list})

	def post(self, request):
		form = PhotoForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			photo = form.save()
			data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
		else:
			data = {'is_valid': False}
		return JsonResponse(data)
def check(request):
	test_datagen = ImageDataGenerator(rescale = 1./255)
	classifier = load_model('main/save_data.h5')
	result_set = test_datagen.flow_from_directory('main/photos/',target_size = (64, 64),batch_size = 32,class_mode = 'binary')
	result = classifier.predict_generator(result_set)

	for i in range(len(result_set.filenames)):
		print(result_set.filenames[i],result[i])

	clear_session()

	del result
	del result_set
	del classifier
	del test_datagen
	return redirect('main/result')

def result(request):
	data={}
	return render(request,'main/result.html',data)