from django.shortcuts import render
from apps.message_form.models import Message

# Create your views here.


def message_form(request):

	if request.method == 'POST':

		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address', '')
		messagestr = request.POST.get('message', '')

		message = Message()
		message.name = name
		message.email = email
		message.address = address
		message.message = messagestr
		message.save()
		return render(request, "message_form.html")

	if request.method == 'GET':

		message = Message.objects.filter()
		if message:
			message = message[0]
			return render(request, "message_form.html", {
				"message": message
			})
		else:
			return render(request, "message_form.html")