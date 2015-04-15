from django.conf.urls import patterns, include, url

from account import views as account_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'axe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^$', account_view.index),
	(r'^login/', account_view.login),
	(r'^logout/', account_view.logout),
	url(r'^account/', include('account.urls')),
)
