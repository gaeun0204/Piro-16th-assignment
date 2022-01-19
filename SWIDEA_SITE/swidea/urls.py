from django.urls import path
from . import views

app_name = "swidea"

urlpatterns = [
	path('', views.swidea_list, name='list'), # 앱 swidea의 urls 파일과 연결
]