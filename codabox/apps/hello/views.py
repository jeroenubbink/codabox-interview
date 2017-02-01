from django.http import HttpResponse
from codabox.apps.hello.models import Greet


def hello(request, id=None):
    name = Greet.objects.get(id=int(id)).name
    return HttpResponse("Hello {}".format(name))
