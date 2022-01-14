from django.shortcuts import render
from .models import Review

def review_list(request):
	reviews = Review.objects.all()
	ctx = {'reviews' : reviews}

	return render(request, template_name = 'list.html', context = ctx)

def review_detail(request, pk):
	review = Review.objects.get(id=pk)
	ctx = {'review' : review}
	
	return render(request, template_name = 'detail.html', context = ctx)