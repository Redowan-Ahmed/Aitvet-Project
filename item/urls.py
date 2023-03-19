from django.urls import path
from . import views

app_name='item'

urlpatterns=[
    path('', views.browse, name='browse'),
    path('new/', views.new_item, name='newitem'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit_item, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
]