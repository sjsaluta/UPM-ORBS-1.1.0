"""ORB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('login/',views.loginPage, name='loginPage'),
    path('google_login/', include('allauth.urls')),
    path('logout/', views.logOutPage, name="logout"),

    path('profile/', views.viewProfile, name="profile"),
    path('profile/edit-profile/',views.editProfile, name='editProfile'),

    #admin pages
    path('manage/',views.manageUsers,name='manageUsers'),
    path('manage/add-user/', views.AddUserPage, name='AddUserPage'),
    path('manage/users/',views.users,name='users'),
    path('manage/edit/<int:pk>',views.editUser, name='editUser'),
    path('manage/edit/change-pass/<int:pk>/',views.changePass,name='changePass'),
    path('delete/<int:pk>',views.deleteUser.as_view(), name='deleteUser'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
