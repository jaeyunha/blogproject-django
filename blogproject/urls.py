"""blogproject URL Configuration

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
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    
    # making a blog object by using html form.
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # making a blog object by using django form 
    path('formcreate/', views.formcreate, name='formcreate'),

    # making a blog object by using django modelform.
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    path('detail/<int:blog_id>', views.detail, name='detail'),

    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),

    path('logout/', accounts_views.logout, name='logout')


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
