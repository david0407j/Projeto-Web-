from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Hola Django</body></html>', content_type='text/html')
