from django.shortcuts import render,redirect
from .models import  ApplicationFormClass,Contact,Bhim_App
import random
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def application(request):
    if request.method=='POST':
        fname         = request.POST.get("fname")
        lname         = request.POST.get("lname")
        dob           = request.POST.get('dob')
        board         = request.POST.get('board')
        father        = request.POST.get("father")
        mother        = request.POST.get("mother")
        qualification = request.POST.get('qualification')
        sname         = request.POST.get('sname')
        saddress      = request.POST.get('Saddress')
        haddress      = request.POST.get('Haddress')
        state         = request.POST.get('state')
        anum          = request.POST.get('anum')
        phonenum      = request.POST.get('num')
        email         = request.POST.get('email')
        number        = '19'+'{:03d}'.format(random.randrange(1, 999))
        username      = (state + board + qualification+ number)
        status        = request.POST.get('hidden1')
        referral      = request.POST.get('referral')
        if ApplicationFormClass.objects.filter(emailID=email).exists():
            return HttpResponse("email id taken in database use another emaild ")
        else:
            af = ApplicationFormClass(firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, state = state, username = username, status=status, referral=referral)
            af.save()
            return redirect('/pay')
    return render(request, 'best/application.html')


def privacypolicy(request):
    return render(request, 'best/privacy.html')


def terms(request):
    return render(request, 'best/terms.html')

def refund(request):
    return render(request, 'best/refund.html')

def six(request):
    return render(request, 'best/six.html')


def home(request):
    return render(request, 'best/home.html')


def seven(request):
    return render(request, 'best/seven.html')


def eight(request):
    return render(request, 'best/eight.html')

def nine(request):
    return render(request, 'best/nine.html')


def ten(request):
    return render(request, 'best/ten.html')

def about(request):
    return render(request, 'best/about.html')


def update(request):
    return render(request, 'best/update.html')


def gallery(request):
    return render(request, 'best/gallery.html')

def brouchars(request):
    return render(request, 'best/brouchars.html')



def contact(request):
    if request.method == 'POST':
        name    =  request.POST.get('form_name')
        email   = request.POST.get('form_email')
        phone   = request.POST.get('form_phone')
        subject = request.POST.get('form_subject')
        message = request.POST.get('form_message')
        add=Contact(name = name, email=email, phone=phone, subject=subject, message=message)
        add.save()
        messages.success(request,"sucessfullu add details and we will contact get back soon")
    return render(request, 'best/contact.html')

def student_login(request):
    return render(request, 'best/studentlogin.html')

def admin_login(request):
    return render(request, 'best/adminlogin.html')

def payment(request):
    return render(request, 'best/pay.html')

def payment2(request):
    return render(request, 'best/payment.html')

def bhimapp(request):
    if request.method=='POST':
        tid  = request.POST['tid']
        tphn = request.POST['tphn']
        add=Bhim_App(transactionid=tid, phoneNumber=tphn)
        add.save()
        return HttpResponse("we will get back soon")
    return render(request, 'best/payment.html')



