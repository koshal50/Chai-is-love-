from django.urls import path
from .import views
from performer import views as performer_views

urlpatterns = [
    path('', views.all_chai, name ='all_chai'),
    path('<int:chai_id>/', views.chai_details, name='chai_details'),
    path('store/', views.chai_store, name='chai_store'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    
    
]
