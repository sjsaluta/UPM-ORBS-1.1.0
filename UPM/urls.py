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
    path('', views.indexPage, name='indexPage'),

    #admin pages
    path('manage-term/',views.manageTerm, name='manageTerm'),
    path('manage-term/add-term/',views.addTerm, name='addTerm'),
    path('manage-term/remove-term/<slug:slug>',views.removeTerm, name='removeTerm'),
    path('manage-term/<slug:slug>/',views.termView, name='termView'),
    path('manage-term/<slug:t>/<slug:r>/',views.deleteRoomTerm, name='deleteRoomTerm'),

    path('manage-college/',views.manageCollege, name='manageCollege'),
    path('manage-college/add-college/',views.addCollege, name='addCollege'),
    path('manage-college/remove/<slug:slug>/',views.removeCollege, name='removeCollege'),
    path('manage-college/<slug:slug>/',views.collegeView, name='adminCollegeView'), 
    path('manage-college/<slug:slug>/add-dept/',views.addDept, name='addDept'),
    path('manage-college/<slug:slug>/add-build/',views.addBuild, name='addBuild'),
    path('manage-college/<slug:c>/remove/<slug:d>/',views.removeDept, name='removeDept'),
    path('manage-college/<slug:c>/remove/<slug:b>/',views.removeBuild, name='removeBuild'),
    path('manage-college/<slug:c>/<slug:b>/',views.buildingView,name='adminBuildingView'),
    path('manage-college/<slug:c>/<slug:b>/remove/<slug:r>',views.removeRoom,name='removeRoom'),
    path('manage-college/<slug:c>/<slug:b>/add-room/',views.addBuildRoom, name='addBuildRoom'),

    path('manage-room/',views.manageRooms, name='manageRooms'), 
    path('manage-room/rooms/',views.rooms, name='rooms'), 
    path('manage-room/edit-room/<slug:slug>/',views.editRoom, name='editRoom'),
    path('manage-room/delete/<int:pk>/',views.deleteRoom,name='deleteRoom'),
    
    #non-admin pages
    path('rooms/',views.roomView,name='roomView'),
    path('rooms/<slug:slug>/calendar-view',views.calendarView, name='calendarView'),

    path('upload/',views.uploadPage,name='uploadPage')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)