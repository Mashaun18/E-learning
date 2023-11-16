from django.urls import path
from .views import homepage, about, courses, contact, testimonial, Ourteam, error


urlpatterns = [
    path("", homepage, name='index'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
    path('testimonial/', testimonial, name='testimonial'),
    path('Ourteam/', Ourteam, name='Ourteam'),
    path('404/', error, name='error'),
]