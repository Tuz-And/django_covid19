from django.shortcuts import render


def home(reqest):
    return render(reqest,"pages/index.html")


def features(reqest):
    return render(reqest,"pages/features.html")


def about_us(reqest):
    return render(reqest,"pages/about_us.html")


def medical_counseling(reqest):
    return render(reqest,"pages/medical-counseling.html")


def medical_research(reqest):
    return render(reqest,"pages/medical-research.html")


def blood_bank(reqest):
    return render(reqest,"pages/blood-bank.html")


def gallery(reqest):
    return render(reqest,"pages/gallery.html")


def blog_archive(reqest):
    return render(reqest,"pages/blog-archive.html")


def blog_archive_with_left_sidebar(reqest):
    return render(reqest,"pages/blog-archive-with-left-sidebar.html")


def blog_archive_with_right_sidebar(reqest):
    return render(reqest,"pages/blog-archive-with-right-sidebar.html")


def error(reqest):
    return render(reqest,"pages/404.html")


def contact(reqest):
    return render(reqest,"pages/contact.html")