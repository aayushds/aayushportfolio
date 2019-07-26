from django.db import models
class Education(models.Model):
    institution = models.CharField(max_length = 75)
    location = models.CharField(max_length = 75)
    degree = models.CharField(max_length = 75)
    course = models.CharField(max_length = 75)
    graddate = models.DateField('Graduation Date')
    grades = models.DecimalField(max_digits = 5, decimal_places = 3)
    def __str__(self):
        return self.institution

class CoursesTaken(models.Model):
    institution = models.ForeignKey('Education', on_delete=models.CASCADE)
    course = models.CharField(max_length = 75)
    grade = models.CharField(max_length = 2)
    def __str__(self):
        return self.course

class Projects(models.Model):
    project_name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    technologies_used = models.CharField(max_length = 300)
    def __str__(self):
        return self.project_name
        
class Skills(models.Model):
    skill_name = models.CharField(max_length = 50)
    level = models.DecimalField(max_digits = 2, decimal_places = 1)
    def __str__(self):
        return self.skill_name