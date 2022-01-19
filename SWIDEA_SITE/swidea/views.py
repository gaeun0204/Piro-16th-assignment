from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import *
from .forms import *

def idea_list(request):
	ideas = Idea.objects.all()
	ctx = {'ideas' : ideas}
	return render(request, template_name = 'list.html', context = ctx)


def plus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest += 1
    idea.save()
    context = {'plus_interest': idea.interest}
    return JsonResponse(context)

def minus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest -= 1
    idea.save()
    context = {'minus_interest': idea.interest}
    return JsonResponse(context)



def idea_detail(request, pk):
	idea = Idea.objects.get(id=pk)
	devtool = idea.devtool # 외래키로 지정한 Devtool 가져옴

	ctx = {'idea' : idea, 'devtool' : devtool}
	return render(request, template_name = 'detail.html', context = ctx)

def idea_create(request):
	if request.method == 'POST':
		form = IdeaForm(request.POST, request.FILES) 
		if form.is_valid():
			form = form.save()
			return redirect('swidea:idea_detail', pk=form.pk)
	else:
		form = IdeaForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'idea_form_register.html', context = ctx)

def idea_update(request, pk):
	idea = get_object_or_404(Idea, id=pk)

	if request.method == 'POST':
		form = IdeaForm(request.POST, request.FILES, instance = idea)
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
			return redirect('swidea:devtool_detail', pk=form.pk)
	else:
		form = DevtoolForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'devtool_register.html', context = ctx)

def devtool_detail(request, pk):
	devtool = Devtool.objects.get(id=pk)
	ideas = Idea.objects.filter(devtool=pk)
	# devool detail 페이지와 동일한 pk를 가진것들을 Idea객체 중에 찾아서 반환

	ctx = {'devtool' : devtool, 'ideas' : ideas}
	return render(request, template_name = 'devtool_detail.html', context = ctx)

def devtool_update(request, pk):
	devtool = get_object_or_404(Devtool, id=pk)

	if request.method == 'POST':
		form = DevtoolForm(request.POST, instance = devtool)
		if form.is_valid():
			devtool = form.save()
			print('pk:', pk)
			return redirect('swidea:devtool_detail', pk)
	else :
		form = DevtoolForm(instance = devtool)
		ctx = {'form' : form}
		return render(request, template_name = 'devtool_update.html', context = ctx)

def devtool_delete(request, pk):
    devtool = get_object_or_404(Devtool, id=pk)
    devtool.delete()
    return redirect('swidea:devtool_list')