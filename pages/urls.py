
from django.urls import path
from pages import views



urlpatterns = [
    path('', views.home, name='home'),
    path('features', views.features, name='features'),
    path('about_us', views.about_us, name='about_us'),
    path('medical-counseling', views.medical_counseling, name='medical_counseling'),
    path('medical-research', views.medical_research, name='medical_research'),
    path('blood-bank', views.blood_bank, name='blood_bank'),
    path('gallery', views.gallery, name='gallery'),
    path('blog-archive', views.blog_archive, name='blog_archive'),
    path('blog-archive-with-left-sidebar', views.blog_archive_with_left_sidebar, name='blog_archive_with_left_sidebar'),
    path('blog-archive-with-right-sidebar', views.blog_archive_with_right_sidebar, name='blog_archive_with_right_sidebar'),
    path('404', views.error, name='error'),
    path('contact', views.contact, name='contact'),


]
