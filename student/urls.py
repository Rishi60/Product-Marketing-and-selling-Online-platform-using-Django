from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as student_views
urlpatterns =[

	url(r'^$', student_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	#url(r'^signup/$', student_views.signup, name='signup'),
	url(r'^signup_success/$', student_views.signup_success, name ='signup_success'),
    url(r'^search/$', student_views.search, name='search'),
    url(r'^buy/$', student_views.buy, name='buy'),
    url(r'^cat/$', student_views.cat, name='cat'),
    url(r'^chart/$', student_views.test_matplotlib, name='chart'),
    url(r'^bargraph/$', student_views.bargraph, name='bargraph'),

]
