"""
URL configuration for learner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings   # to load media files during development
from django.conf.urls.static import static   # to load media files during development
from .import views
from learner import views as project_views
from performer import views as performer_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'  ),
   # path('about/', views.about, name ='about'  ),
    path('contact/', views.contact, name ='contact'  ),
    path('performer/', include('performer.urls')), # transfers the control to the app through include function
    path('about/<int:pk>/', performer_views.about_detail, name='about_detail'),


    path("__reload__/", include("django_browser_reload.urls")), # enables auto-reload during development
    path('accounts/signup/', performer_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # provides login, logout, password reset
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # to load media files during development

