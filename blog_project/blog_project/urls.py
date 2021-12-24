"""blog_project URL Configuration

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

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # Added for login, logout, sign in
    path('accounts/', include('accounts.urls')),  # Points to the urls files in the 'accounts' app created. The order of
    # our urls matters here because Django reads this file top-to-bottom. Therefore when we request them
    # /accounts/signup url, Django will first look in auth, not find it, and then proceed to the accounts app
    path('', include('blog.urls')),  # Points to the urls files in the 'blog' app created
    path('admin/', admin.site.urls),
]
