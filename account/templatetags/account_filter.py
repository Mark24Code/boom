# -*- coding:utf-8 -*-

import time
from datetime import timedelta, datetime, date

from django import template
from django.core.cache import cache
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q

from account.models import *
from datetime import datetime

register = template.Library()


@register.filter(name='get_customer_number')
def get_customer_number(id):
	return id + 10000