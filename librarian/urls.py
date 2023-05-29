from django.conf.urls import url
#from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as librarian_views
urlpatterns =[

	url(r'^$', librarian_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login1.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out1.html'}, name='logout'),
	url(r'^signup/$', librarian_views.signup, name='signup'),
	url(r'^signup_success/$', librarian_views.signup_success, name ='signup_success'),
	url(r'^add_book/$',librarian_views.add_book, name='add_book'),
]
