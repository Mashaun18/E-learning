from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Course, TeamMember, Testimonial

# Create your views here.
def homepage(request):
    return render(request, 'education/index.html')

def about(request):
    return render(request, 'education/about.html')

def contact(request):
    if request.method == "POST":
        input_name = request.POST.get("name")
        input_email = request.POST.get("email")
        input_subject = request.POST.get("subject")
        input_message = request.POST.get("message")

        if len(input_name) > 100:
            messages.error(request, "name is too long")
            return redirect("contact")
        
        elif input_subject == "":
            messages.error(request, "subject cannot be empty")
            return redirect("contact")
        elif input_email == "":
            messages.error(request, "email cannot be empty")
            return redirect("contact")
        elif input_message == "":
            messages.error(request, "message cannot be empty")
            return redirect("contact")
        else:
            Contact.objects.create(name=input_name, email=input_email, subject=input_subject, message=input_message)
            messages.success(request, "Thank you for contacting us")
            return redirect("/")

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

def error(request):
    return render(request, 'education/404.html')