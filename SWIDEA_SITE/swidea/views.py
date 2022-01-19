from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def swidea_list(request):
	ideas = Idea.objects.all()
	ctx = {'ideas' : ideas}
	return render(request, template_name = 'list.html', context = ctx)

def swidea_detail(request, pk):
	idea = Idea.objects.get(id=pk)
	ctx = {'idea' : idea}
	return render(request, template_name = 'detail.html', context = ctx)

def swidea_create(request):
	if request.method == 'POST':
		form = IdeaForm(request.POST) 
		if form.is_valid():
			form = form.save()
			return redirect('swidea:list')
	else:
		form = IdeaForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'idea_form.html', context = ctx)
