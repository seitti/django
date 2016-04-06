from django.shortcuts import render
# from .models import Message


def home(request):
    # messages = Message.objects.order_by('order')
    messages = [r'Első', r'Második', r'Harmadik']
    context_dict = {
        'messages': messages
    }
    return render(request, 'starter_app/home.html', context_dict)
