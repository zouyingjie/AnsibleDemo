from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world")


class AnsibleLessonView(TemplateView):
    template_name = "ansible_hello.html"


class HelloAnsibleView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello ansible")


class HelloSuperView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello SUPER")
