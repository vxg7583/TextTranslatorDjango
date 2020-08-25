from django.shortcuts import render
from .models import Translator
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from google.cloud import translate_v2 as translate_google
# translate_client = translate_google.Client()
# Create your views here.


class Translate(ListView):
    def index(request):
        queryset = request.GET.get('message')

        return render(request, 'translator/index.html', {'queryset':queryset})
