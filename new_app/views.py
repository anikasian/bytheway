from django.http import HttpResponse


# Create your views here.
def new_app(request):
    return HttpResponse("Hello, World!")
