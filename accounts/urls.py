from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', login, {'template_name': 'accounts/login.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/', logout, {'next_page': 'core:index'}, name='logout'),
    url(r'^alterar-dados/', views.update_user, name='update_user'),
    url(r'^alterar-senha/', views.update_password, name='update_password'),
    url(r'^registro/', views.register, name='register'),
]
