from django.shortcuts import render
from .models import *

# Create your views here.
def swidea_list(request):
	ideas = Idea.objects.all()
	ctx = {'ideas' : ideas}
	return render(request, template_name = 'list.html', context = ctx)

def swidea_detail(request, pk):
	idea = Idea.objects.get(id=pk)
	ctx = {'idea' : idea}
	return render(request, template_name = 'detail.html', context = ctx)