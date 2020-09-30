from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('data/', views.data, name='data'),
    path('data/outliers', views.outliers, name='outliers'),
    path('wineTable/', views.wineTable, name='wineTable'),
    # path('accounts/login/', views.login, name='login'),
    # url(r'^login/$', auth_views.login, {'template_name': 'templates/login.html'}, name='login'),
    # url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^login/$', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

]