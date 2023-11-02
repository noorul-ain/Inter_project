from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='homepage'),
    path('dell/<int:id>', views.delete_data, name='deletedata'),
    path('up/<int:id>', views.update_data, name='updatedata'),

]
