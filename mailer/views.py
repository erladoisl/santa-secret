from typing import Dict, List
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
from .utils.gift import play_game

def sendMail(request):

    print(42)
    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':
        print(43)

        form = EmailForm(request.POST)
        members = get_members(request.POST)

        print(f'All Members: {members}')
        messageSent = True
        play_game(members)

    else:
        print(44)
        form = EmailForm()

    return render(request, 'index.html', {

        'form': form,
        'messageSent': messageSent,

    })


def get_members(request) -> List[Dict[str, str]]:
    i = 0 
    res = []
    
    while request.get(f'firstName{i}', '') != '':
        res.append({'name': request.get(f'firstName{i}', ''),
                    'email': request.get(f'email{i}', '')})
        i += 1

    return res
