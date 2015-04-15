# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group, User


class Customer(models.Model):
	owner = models.ForeignKey(User) #所属帐号
	name = models.CharField(max_length=50) #客户名称
	tel_number = models.CharField(max_length=50) #客户电话 
	plate_number = models.CharField(max_length=50) #车牌号码
	vehicle_brand = models.CharField(max_length=50) #车辆品牌
	motorcycle_type = models.CharField(max_length=50) #车辆型号
	mileage = models.CharField(max_length=50) #公里数
	adress = models.CharField(max_length=150) #客户地址 
	remark = models.TextField(max_length=150) #备注
	created_at = models.DateTimeField(auto_now_add=True) #创建时间

	class Meta(object):
		db_table = 'account_customer'
		ordering = ['id',]


class PurchaseHistory(models.Model):
	customer = models.ForeignKey(Customer)
	mileage = models.CharField(max_length=50) #公里数
	oil_type = models.CharField(max_length=50) #机油型号
	oil_filter = models.CharField(max_length=50) #机滤
	air_filter = models.CharField(max_length=50) #空滤
	steam_filter = models.CharField(max_length=50) #汽滤
	other_products = models.CharField(max_length=150) #其它产品 
	price = models.CharField(max_length=10) #价格
	remark = models.TextField(max_length=150) #备注
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True) #创建时间

	class Meta(object):
		db_table = 'account_purchase_history'
		ordering = ['id',]