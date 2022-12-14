"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from apps.settings.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', include('apps.settings.urls') ),
    path('users/', include('apps.users.urls')),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = 'logout'),
    path('', include('apps.places.urls') ),
    path('hotel/', include('apps.hotels.urls')),
    path('accounts/', include('allauth.urls')),
   
]
    
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#1048720379987-4j6hti6u118p6ucn5advuu6umm99c1pv.apps.googleusercontent.com Client
##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