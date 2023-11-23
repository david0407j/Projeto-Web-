from django.http import HttpResponse


def home(request):
    return HttpResponse('Deus e mais ')
