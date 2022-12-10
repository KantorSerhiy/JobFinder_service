from django.shortcuts import render

from scraping.models import Vacancy


def index(request):
    qs = Vacancy.objects.all()

    context = {
        "obj_list": qs
    }
    return render(request, "scraping/home.html", context=context)
