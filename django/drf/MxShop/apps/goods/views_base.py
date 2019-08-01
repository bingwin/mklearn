import json

from django.views.generic.base import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from goods.models import Goods


class GoodsListView(View):

	def get(self, request):
		'''
		实现商品列表页
		:param request:
		:return:
		'''
		goods = Goods.objects.all()[0:10]
		json_data = serializers.serialize('json', goods)
		return HttpResponse(json_data, content_type='application/json')
