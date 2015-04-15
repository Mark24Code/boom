# -*- coding: utf-8 -*-

from django.conf.urls import *
from account import views

urlpatterns = patterns('',
	(r'^$', views.index),
	(r'^list_customers/', views.list_customers),
	(r'^api/customer/create/', views.create_customer),
	(r'^api/customer/edit/', views.edit_customer),
	# (r'^del/', views.delete_product),

	(r'^view_customer/(\d+)/', views.view_customer),
	(r'^api/log/create/', views.create_log),
	(r'^api/log/delete/', views.delete_log),
)