from django.contrib import admin
from django.urls import path

from icoderApp import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.showhome,name='home'),
   path("about",views.showAbout,name='about'),
   #path("topic",views.topic,name="topic"),
   path("contact",views.contact,name='contact'),
   path("tec/",views.tec,name='tec'),
   #path("contact/",views.contact,name='contact'),
   
]
