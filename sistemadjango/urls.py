"""sistemadjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import login, base, lista_user, cadastrar_user, atualizar_perfil

urlpatterns = [ 
	url(r'^$', login, name='login'),   
	url(r'^base/$', base, name='home'),
	url(r'^lista_user/$', lista_user, name='lista_user'),
	url(r'^cadastrar_user/$', cadastrar_user, name='cadastrar_user'),
	url(r'^atualizar_perfil/$', atualizar_perfil, name='perfil'),
    url(r'^admin/', admin.site.urls),
]
