from django.urls import path
from . import views

app_name = "swidea"

urlpatterns = [
	path('', views.idea_list, name = 'idea_list'), # 앱 swidea의 urls 파일과 연결
	path('<int:pk>/', views.idea_detail, name = 'idea_detail'),
	path('create/', view = views.idea_create, name = 'idea_create'),
	path('<int:pk>/update', view = views.idea_update, name = 'idea_update'),
	path('<int:pk>/delete', view = views.idea_delete, name = 'idea_delete'),
]