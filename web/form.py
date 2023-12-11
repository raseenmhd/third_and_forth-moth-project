from django import forms
from .models import user
f

class PersonData(forms.Form):
	class meta:
		model = user
		fields = '__all__'