"""todo URL Configuration

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
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('signup/', views.signup, name='signup'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('showtodo/<int:todo_id>/', views.showtodo, name='showtodo'),
    path('add_photo/<int:todo_id>/', views.add_photo, name='add_photo'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)