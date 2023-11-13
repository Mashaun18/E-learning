from django.shortcuts import render
from.models import Course, TeamMember, Testimonial

# Create your views here.
def homepage(request):
    return render(request, 'education/index.html')

def about(request):
    return render(request, 'education/about.html')

def contact(request):
    return render(request, 'education/contact.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'education/courses.html')

def Ourteam(request):
    team_members = TeamMember.objects.all()
    return render(request, 'education/team.html')

def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'education/testimonial.html')