from django.shortcuts import render
from .models import Translator
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
# from google.cloud import translate_v2 as translate_google
# translate_client = translate_google.Client()
# Create your views here.


class Translate(ListView):
    def index(request):
        
        if request.GET.get('message'):
            queryset = request.GET.get('message')
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1'}
            data = {'sl':'en','tl':'hi', 'q':queryset}


            response = requests.post('https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=%25s&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e&', headers=headers, params=data)
            queryset = response.json()


        else:
            queryset = "Please Enter something in the above text area."

        # Do something with user input

        return render(request, 'translator/index.html', {'queryset':queryset})
