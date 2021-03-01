from django.contrib import admin
from django.urls import path
from rest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view),
    path('class1/', views.FirstClassView.as_view()),
    path('class2/', views.SecondClassView.as_view())
]
