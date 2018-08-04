from .models import *

class PhotoForm(forms.ModelForm):
	class Meta:
		model=Photo
		fields=('file',)