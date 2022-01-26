from django.urls import path 
from . import views

app_name = 'main'

urlpatterns = [
	path('', view = views.post_list, name = 'list'),
	path('create/', view = views.post_create, name = 'create'),
	path('like', views.like, name='like'),
]