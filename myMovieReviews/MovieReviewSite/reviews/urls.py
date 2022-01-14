from django.urls import path 

app_name = 'posts'

urlpatterns = [
    path('list/', post_list),
	path('create/', ),
]