from re import template
from tkinter.tix import Tree

from matplotlib.style import context
from .models import userData
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    template=loader.get_template('login.html')
    
    return HttpResponse(template.render({},request))

def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))

def signupprocess(request):        
        first=request.POST['first']
        last=request.POST['last']
        dob=request.POST['dob']
        mob=request.POST['mob'] 
        Email=request.POST['Email']
        user=request.POST['AcType']
        username=request.POST['username']
        passs=request.POST['passs']
        usernameCount=len(userData.objects.filter(username=username))
        emailCount=len(userData.objects.filter(email_id=Email))
        if(usernameCount or emailCount):
            template=loader.get_template('signup.html')
            return HttpResponseRedirect(reverse('signup'))
        else:    
            member=userData(firstname=first,lastname=last,DOB=dob,mobile=mob,email_id=Email,user=user,username=username,password=passs)
            member.save()
            return HttpResponseRedirect(reverse('index'))   


    
def loginprocess(request):
    username=request.POST['username']
    password=request.POST['password']
    no_data=len(userData.objects.filter(username=username,password=password))
    # member=userData.objects.get(username=username)
    if(no_data):
        template=loader.get_template('access.html')
        return HttpResponse(template.render({},request))
    else:
        return HttpResponseRedirect(reverse('index'))