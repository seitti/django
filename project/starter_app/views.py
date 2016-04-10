import json
from django.shortcuts import render
# from .models import Message

f = open(r'c:\pylvax\django\project\starter_app\new_content.json', 'r')
data = json.load(f)

def home(request):
    # messages = Message.objects.order_by('order')
    # messages = ['Első', 'Második', 'Harmadik']
    # context_dict = {
        # 'messages': messages
    # }
    context_dict = data

    return render(request, 'starter_app/home.html', context_dict)
