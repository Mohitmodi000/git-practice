from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("userlogin/",views.user,name="user"),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    ]