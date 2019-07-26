from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.index, name='index'),
    path('education/', views.education, name = 'education'),
    path('projects/', views.projects, name = 'projects'),
    path('skills/', views.skills, name = 'skills'),
    path('resume/', views.resume, name = 'resume'),
    path('contact/', views.contact, name = 'contact'),
    path('thanks/',views.thanks, name = 'thanks'),
    path('courses/', views.courses, name = 'courses')
]