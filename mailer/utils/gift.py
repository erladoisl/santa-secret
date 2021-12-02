import random
from django.core.mail import send_mail
from django.conf import settings


participants = []
subject = 'Сообщение от службы Тайного Санты'

def distribute_recipients(participants):
    random.shuffle(participants)

    for i, participant in enumerate(participants):
        gift_to = participants[i - 1] if i > 0 else participants[-1]
        participant['gift to'] = gift_to['name']

    return participants

#print(distribute_recipients(participants))
def sent_message(subject, message, email):
    send_mail(subject, message,
                settings.DEFAULT_FROM_EMAIL, [email])

def play_game(members = participants):
    distributed = distribute_recipients(members)

    for participant in distributed:
        message = f'{participant["name"]}, вашим подопечным выбран {participant["gift to"]}. '
        #print(message)
        sent_message(subject, message, participant['email'])