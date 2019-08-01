from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from django.conf import settings


# 生成随机字符串
def random_str(randomlength=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str += chars[random.randint(0, length)]
	return str


def send_register_email(email, send_type="register"):
	email_record = EmailVerifyRecord()
	if send_type == "update_email":
		code = random_str(4)
	else:
		code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()

	email_title = ""
	email_body = ""

	if send_type == "register":
		email_title = u"激活链接"
		email_body = u"请点击下面的链接激活你的账号: http://192.168.153.151:5555/active/{0}".format(code)

		send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
		if send_status:
			pass

	elif send_type == "forget":
		email_title = u"注册密码重置链接"
		email_body = u"请点击下面的注册密码重置链接: http://192.168.153.151:5555/reset/{0}".format(code)

		send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
		if send_status:
			pass

	elif send_type == "update_email":
		email_title = u"修改邮箱验证码"
		email_body = u"你的验证码是{0}".format(code)

		send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
		if send_status:
			pass