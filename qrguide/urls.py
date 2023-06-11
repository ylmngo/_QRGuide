from django.urls import path 

from . import views 

urlpatterns = [
    path('college/', views.college_view, name='college'), 
    path('college/block/<int:block_id>', views.block_view, name='block'), 
    path('college/block/<int:block_id>/floor/<int:floor_id>/marker/<int:marked>/', views.floor_view, name='floor'), 
]