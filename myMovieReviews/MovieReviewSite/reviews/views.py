from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
	reviews = Review.objects.all()
	ctx = {'reviews' : reviews}
	return render(request, template_name = 'list.html', context = ctx)

def review_detail(request, pk):
	review = Review.objects.get(id=pk)
	ctx = {'review' : review}
	return render(request, template_name = 'detail.html', context = ctx)

def review_create(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST) 
		if form.is_valid():
			form = form.save()
			return redirect('reviews:list')
	else:
		form = ReviewForm() 
		ctx = {'form' : form}
		return render(request, template_name = 'review_form.html', context = ctx)