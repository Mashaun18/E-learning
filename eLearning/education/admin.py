from django.contrib import admin
from .models import Course, TeamMember, Testimonial 

# Register your models here.
admin.site.register([Course, TeamMember, Testimonial])
