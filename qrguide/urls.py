from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index_view, name='index'), 
    path('about/', views.about_view, name='about'), 
    path('about/<str:person>', views.about_person_view, name='about-aamer'), 
    path('college/', views.college_view, name='college'), 
    path('college/block/<int:block_id>', views.block_view, name='block'), 
    path('college/block/<int:block_id>/floor/<int:floor_id>/marker/<int:marked>/', views.floor_view, name='floor'), 
] 