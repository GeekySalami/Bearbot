"""
URL configuration for Bearbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_view
from build import views as workspce_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    #path('', include('users.urls')),
    #path('', include('text_editor.urls')),
    path('', include('blog.urls')),
    path('', include('learn.urls')),
    #path('', include('resource_viewer.urls')),
    path('workspace/', include('build.urls')),
    path('profile/', users_view.profile, name ='profile'),
    path('register/', users_view.register, name ='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name ='logout', ),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name ='login'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)