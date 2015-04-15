# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q

from core.paginator import paginate
from core.jsonresponse import create_response, JsonResponse
from models import *


#===============================================================================
# login : 登录
#===============================================================================
def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user:
			auth.login(request, user)
			return HttpResponseRedirect('/account/list_customers/')
		else:
			#用户名密码错误
			c = RequestContext(request, {
				'errorMsg': u'用户名或密码错误'
			})
			return render_to_response('account/login.html', c)
	else:
		c = RequestContext(request, {
		})
		return render_to_response('account/login.html', c)


#===============================================================================
# index : 用户首页
#===============================================================================
@login_required(login_url='/login/')
def index(request):
	return HttpResponseRedirect('/account/list_customers/')


#===============================================================================
# logout : 登出
#===============================================================================
@login_required(login_url='/login/')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login/')


#===============================================================================
# list_customers : 客户列表
#===============================================================================
@login_required(login_url='/login/')
def list_customers(request):
	page = int(request.GET.get('page', 1))
	count = int(request.GET.get('count_per_page', 20))
	keyword = request.GET.get('keyword', '').strip()
	customers = Customer.objects.filter(owner=request.user)
	if keyword:
		customers = customers.filter(Q(tel_number__icontains=keyword) | Q(plate_number__icontains=keyword) | Q(name__icontains=keyword))
	pageinfo, customers = paginate(customers, page, count, query_string=request.META['QUERY_STRING'])
	c = RequestContext(request, {
		'customers': customers,
		'pageinfo': pageinfo.to_dict(),
		'keyword': keyword
	})
	return render_to_response('account/list_customers.html', c)


#===============================================================================
# create_customer : 创建客户
#===============================================================================
@login_required(login_url='/login/')
def create_customer(request):
	name = request.POST.get('name','')
	tel_number = request.POST.get('tel_number','')
	plate_number = request.POST.get('plate_number','')
	vehicle_brand = request.POST.get('vehicle_brand','')
	motorcycle_type = request.POST.get('motorcycle_type','')
	mileage = request.POST.get('mileage','')
	adress = request.POST.get('adress','')
	remark = request.POST.get('remark','')

	Customer.objects.create(
		owner = request.user,
		name = name,
		tel_number = tel_number,
		plate_number = plate_number,
		vehicle_brand = vehicle_brand,
		motorcycle_type = motorcycle_type,
		mileage = mileage,
		adress = adress,
		remark = remark
	)
	response = create_response(200)
	return response.get_response()


#===============================================================================
# edit_customer : 编辑客户
#===============================================================================
@login_required(login_url='/login/')
def edit_customer(request):
	if request.GET:
		customer_id = request.GET.get('customer_id','')
		customer = Customer.objects.get(id=customer_id)
		customer_json = JsonResponse()
		customer_json.id = customer.id
		customer_json.name = customer.name
		customer_json.tel_number = customer.tel_number
		customer_json.plate_number = customer.plate_number
		customer_json.vehicle_brand = customer.vehicle_brand
		customer_json.motorcycle_type = customer.motorcycle_type
		customer_json.mileage = customer.mileage
		customer_json.adress = customer.adress
		customer_json.remark = customer.remark
		response = create_response(200)
		response.data.customer = customer_json
		return response.get_jsonp_response(request)
	elif request.POST:
		customer_id = request.POST.get('customer_id','')
		name = request.POST.get('name','')
		tel_number = request.POST.get('tel_number','')
		plate_number = request.POST.get('plate_number','')
		vehicle_brand = request.POST.get('vehicle_brand','')
		motorcycle_type = request.POST.get('motorcycle_type','')
		mileage = request.POST.get('mileage','')
		adress = request.POST.get('adress','')
		remark = request.POST.get('remark','')
		
		Customer.objects.filter(id=customer_id).update(
			name = name,
			tel_number = tel_number,
			plate_number = plate_number,
			vehicle_brand = vehicle_brand,
			motorcycle_type = motorcycle_type,
			mileage = mileage,
			adress = adress,
			remark = remark
		)
		response = create_response(200)
		return response.get_response()


#===============================================================================
# view_customer : 查看客户
#===============================================================================
@login_required(login_url='/login/')
def view_customer(request, customer_id):
	"""
		查看客户
	"""
	customer = Customer.objects.get(id=customer_id)
	purchase_histories = PurchaseHistory.objects.filter(customer_id=customer_id, is_deleted=False)

	c = RequestContext(request, {
		'customer': customer,
		'purchase_histories': purchase_histories,
	})
	return render_to_response('account/view_customer.html', c)


#===============================================================================
# create_log : 新增购买记录
#===============================================================================
@login_required(login_url='/login/')
def create_log(request):
	customer_id = request.POST['customer_id']
	mileage = request.POST.get('mileage','')
	oil_type = request.POST.get('oil_type','')
	oil_filter = request.POST.get('oil_filter','')
	air_filter = request.POST.get('air_filter','')
	steam_filter = request.POST.get('steam_filter','')
	other_products = request.POST.get('other_products','')
	price = request.POST.get('price','')
	remark = request.POST.get('remark','')

	customer = Customer.objects.get(id=customer_id)
	PurchaseHistory.objects.create(
		customer = customer,
		mileage = mileage,
		oil_type = oil_type,
		oil_filter = oil_filter,
		air_filter = air_filter,
		steam_filter = steam_filter,
		other_products = other_products,
		price = price,
		remark = remark
	)
	response = create_response(200)
	return response.get_response()


#===============================================================================
# delete_log : 删除购买记录
#===============================================================================
@login_required(login_url='/login/')
def delete_log(request):
	log_id = request.GET['log_id']
	try:
		PurchaseHistory.objects.filter(id=log_id).update(is_deleted=True)
	except:
		pass

	response = create_response(200)
	return response.get_response()