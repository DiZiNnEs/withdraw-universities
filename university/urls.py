from django.urls import path

from university import views

urlpatterns = [
    path('', views.main, name='index'),
    path('university/<str:pk>', views.university_page_delete, name='university_page'),
]
