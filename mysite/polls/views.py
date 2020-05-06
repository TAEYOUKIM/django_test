from django.http import HttpResponse


def index(request):
    return HttpResponse("Test for developer's environment")