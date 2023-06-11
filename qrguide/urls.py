from django.urls import path 

from . import views 

urlpatterns = [
    path('college/', views.college_view), 
    path('college/block/<int:block_id>', views.block_view), 
]