from django import forms
from .models import *

class IdeaForm(forms.ModelForm):
	class Meta:
		model = Idea
		fields = '__all__'