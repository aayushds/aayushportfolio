import json
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.core.mail import EmailMultiAlternatives

from .models import Education, Projects, Skills, CoursesTaken
from .forms import Emailform

def index(request):
    template = loader.get_template('cv/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def education(request):
    myinst = Education.objects.all()
    template = loader.get_template('cv/edu.html')
    context = {
        'myinst':myinst,
    }
    return HttpResponse(template.render(context, request), RequestContext(request))

def courses(request):
    if request.method == 'GET':
        inst = request.GET['inst_id']
        course_grade = CoursesTaken.objects.filter(institution__id=inst)
        course_grade_dict = {}
        for course_grades in course_grade:
            course_dict = {course_grades.course:course_grades.grade}
            course_grade_dict.update(course_dict)
        print(course_grade_dict)
    return HttpResponse(
            json.dumps(course_grade_dict),
            content_type="application/json",        
        )
    
def projects(request):
    mypro = Projects.objects.all()
    template = loader.get_template('cv/projects.html')
    context = {
        'mypro':mypro,
    }
    return HttpResponse(template.render(context, request))
    
def resume(request):
    template = loader.get_template('cv/resume.html')
    context = {}
    return HttpResponse(template.render(context, request))

def skills(request):
    myskills = Skills.objects.all()
    template = loader.get_template('cv/skills.html')
    context = {
        'myskills':myskills,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('cv/contact.html')

    if request.method == 'POST':
        myform = Emailform(request.POST)
        if myform.is_valid():
            name = myform.cleaned_data['name']
            emailid = myform.cleaned_data['emailid']
            subject = myform.cleaned_data['subject']
            comment = myform.cleaned_data['comment']
            recipient = 'aayushshah77@gmail.com'
            subject, from_email, to = subject, recipient, recipient
            msg = EmailMultiAlternatives(subject, comment, from_email, [to])
            msg.send()
            return HttpResponseRedirect('/cv/thanks/')
    else:
        myform = Emailform()
    return HttpResponse(template.render({'myform':myform}, request))
    
def thanks(request):
    template = loader.get_template('cv/thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))