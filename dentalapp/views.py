from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail 


def home(request):
    return render(request,"home.html" ,{})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		
		send_mail(
		    'Appoiment Fixed at Dento ' + message_name,   #subject Part
		    
			message + '       This mail send by our Patients Please contact :' + message_email, #message part with the rreply email
            message_email,        #from_email with title
            ['biswaranjanroul2@gmail.com'],   #reciver email
            fail_silently = False,
			)  

		return render(request, "contact.html" ,{'message_name' :message_name} )
 	             

	else:
		return render(request, "contact.html" ,{} )
def about(request):
	return render(request ,"about.html", {})
def blog(request):
	return render(request ,"blog.html",{})
def blog_details(request):
	return render(request ,"blog-details.html",{})
def service(request):
	return render(request ,"service.html",{})	
def pricing(request):
	return render(request ,"pricing.html",{})		



 


