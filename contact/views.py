from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_massege(request):
    myinfo=Info.objects.first()
    if request.method=='POST':
        email=request.POST['email']
        subject=request.POST['subject']
        massege=request.POST['message']
        send_mail(
            subject,
            massege,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request,'contact/contact.html',{'myinfo':myinfo})