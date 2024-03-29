"""FacheritasCafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #apps funcionalidades django
    path('admin/', admin.site.urls),    
    path('login/', include('login.urls'), name= 'login'),

    #Apps especificas
    path('', include('Dashboard.urls'), name= 'Dashboard'),
    path('Menu/', include('Menu.urls'), name='Menu'),
    path('Orden/', include('Comanda.urls'), name='Comanda'),
    path('Ventas/', include('Venta.urls'), name='Venta')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
