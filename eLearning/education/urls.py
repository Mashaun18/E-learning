from django.urls import path
from .views import homepage, about, courses, contact, testimonial, Ourteam

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('courses/', views.courses, name='courses'),
#     path('contact/', views.contact, name='contact'),
#     path('testimonials/', views.testimonials, name='testimonials'),
#     path('team/', views.team, name='team'),
    
# ]

urlpatterns = [
    path("", homepage),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
    path('testimonial/', testimonial, name='testimonial'),
    path('Ourteam/', Ourteam, name='Ourteam'),
]