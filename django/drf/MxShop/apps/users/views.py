from random import choice

from MxShop.settings import APIKEY
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .models import UserProfile, VerifyCode
from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer
from utils.yunpian import YunPian

# Create your views here.


class CustomBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		try:
			user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	发送短信验证码
	"""
	serializer_class = SmsSerializer

	def generate_code(self):
		"""
		生成四位数字的验证码
		:return:
		"""
		seeds = "1234567890"
		random_str = []
		for i in range(4):
			random_str.append(choice(seeds))

		return "".join(random_str)

	# 重写 create 方法
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		mobile = serializer.validated_data["mobile"]

		yun_pian = YunPian(APIKEY)

		code = self.generate_code()

		sms_status = yun_pian.send_sms(code=code, mobile=mobile)

		if sms_status["code"] != 0:
			return Response({
				"mobile": sms_status["msg"]
			}, status=status.HTTP_400_BAD_REQUEST)
		else:
			code_record = VerifyCode(code=code, mobile=mobile)
			code_record.save()
			return Response({
				"mobile": mobile
			}, status=status.HTTP_201_CREATED)


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	"""
	用户
	"""
	serializer_class = UserRegSerializer
	queryset = UserProfile.objects.all()
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

	def get_serializer_class(self):
		if self.action == "retrieve":
			return UserDetailSerializer
		elif self.action == "create":
			return UserRegSerializer

		return UserDetailSerializer

	# permission_classes = (IsAuthenticated, )
	def get_permissions(self):
		if self.action == "retrieve":
			return [IsAuthenticated()]
		elif self.action == "create":
			return []

		return []

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)

		re_dict = serializer.data
		payload = jwt_payload_handler(user)
		re_dict['token'] = jwt_encode_handler(payload)
		re_dict["name"] = user.name if user.name else user.username

		headers = self.get_success_headers(serializer.data)
		return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

	def get_object(self):
		return self.request.user

	def perform_create(self, serializer):
		return serializer.save()


