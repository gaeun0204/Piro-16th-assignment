from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def idea_list(request):
	ideas = Idea.objects.all()
	ctx = {'ideas' : ideas}
	return render(request, template_name = 'list.html', context = ctx)

def idea_detail(request, pk):
	idea = Idea.objects.get(id=pk)
	ctx = {'idea' : idea}
	return render(request, template_name = 'detail.html', context = ctx)

def idea_create(request):
	if request.method == 'POST':
		form = IdeaForm(request.POST) 
		if form.is_valid():
			form = form.save()
			return redirect('swidea:idea_list')
	else:
		form = IdeaForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'idea_form_register.html', context = ctx)

def idea_update(request, pk):
	idea = get_object_or_404(Idea, id=pk)

	if request.method == 'POST':
		form = IdeaForm(request.POST, instance = idea) #
		if form.is_valid():
			idea = form.save()
			return redirect('swidea:idea_detail', pk)
	else :
		form = IdeaForm(instance = idea)
		ctx = {'form' : form}
		return render(request, template_name = 'idea_form_update.html', context = ctx)

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    idea.delete()
    return redirect('swidea:idea_list')


def devtool_list(request):
	devtools = Devtool.objects.all()
	ctx = {'devtools' : devtools}
	return render(request, template_name = 'devtool_list.html', context = ctx)

def devtool_create(request):
	if request.method == 'POST':
		form = DevtoolForm(request.POST) 
		if form.is_valid():
			form = form.save()
			return redirect('swidea:devtool_list')
	else:
		form = DevtoolForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'devtool_register.html', context = ctx)