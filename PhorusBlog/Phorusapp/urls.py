from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('contact/',views.contact,name='contact'),
    path('akin/',views.akin,name='akin'),
    path('greeting/',views.greeting,name='greeting'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]