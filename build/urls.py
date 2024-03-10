from . import views
from django.urls import path

urlpatterns = [
	path('', views.wrkspace, name = 'wrkspce'),
	path('execute_code/', views.execute_code, name = 'wrkspce')


]