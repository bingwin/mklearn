from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage, Banner, GoodsCategoryBrand, IndexAd, HotSearchWords
from django.db.models import Q


class GoodCatgorySerializer3(serializers.ModelSerializer):
	"""
	商品类别序列化3类
	"""

	class Meta:
		model = GoodsCategory
		fields = '__all__'


class GoodCatgorySerializer2(serializers.ModelSerializer):
	"""
	商品类别序列化2类
	"""
	sub_cat = GoodCatgorySerializer3(many=True)

	class Meta:
		model = GoodsCategory
		fields = '__all__'


class GoodCatgorySerializer(serializers.ModelSerializer):
	"""
	商品类别序列化1类
	"""
	sub_cat = GoodCatgorySerializer2(many=True)

	class Meta:
		model = GoodsCategory
		fields = '__all__'


class GoodsImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = GoodsImage
		fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
	category = GoodCatgorySerializer()
	images = GoodsImageSerializer(many=True)

	class Meta:
		model = Goods
		fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banner
		fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = GoodsCategoryBrand
		fields = '__all__'


class IndexCategorySerializer(serializers.ModelSerializer):
	# Brand指向的是GoodsCategory,那一个GoodsCategory有多个Brand,所以many=True
	brands = BrandSerializer(many=True)
	goods = serializers.SerializerMethodField()
	sub_cat = GoodCatgorySerializer2(many=True)
	ad_goods = serializers.SerializerMethodField()

	def get_ad_goods(self, obj):
		goods_json = {}
		ad_goods = IndexAd.objects.filter(category_id=obj.id)
		if ad_goods:
			good_ins = ad_goods[0].goods
			goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
		return goods_json

	def get_goods(self, obj):
		all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
			category__parent_category__parent_category_id=obj.id))
		goods_serializer = GoodsSerializer(all_goods, many=True)
		return goods_serializer.data


	class Meta:
		model = GoodsCategory
		fields = '__all__'


class HotWordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = HotSearchWords
		fields = "__all__"