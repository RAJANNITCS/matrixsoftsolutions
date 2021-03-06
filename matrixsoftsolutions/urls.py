"""matrixsoftsolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from matrixApp import views
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('post_list/', views.post_list_view),
    path('fileManager/', views.soft_detail),
    path('vpadNotepad/', views.soft_detail1),
    path('about/', views.about),
    path('download/', views.Download),
    path('/tag/<str:tag_slug>/', views.post_list_view,name='post_list_by_tag_name'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/', views.post_detail_view,name='post_detail'), 
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 