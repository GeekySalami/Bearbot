from . import views
from django.urls import path

urlpatterns = [
	path('', views.wrkspace, name = 'wrkspce'),
	path('run_code/', views.run_code, name = 'runcode')
]