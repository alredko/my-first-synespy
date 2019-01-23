from django.http import HttpResponse
from django.shortcuts import render
from .models import Word
import json

def status_list(request):
    status = Word.objects.filter(num=1)
    return render(request, {'status': status})

def word_list_01(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        w = DeckOfCards[0]
        words = Word.objects.get(num = w[1])
    return render(request, '01.html', {'words': words})

def word_list_02(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        w = DeckOfCards[0]
        words = Word.objects.get(num = w[1])
    return render(request, '02.html', {'words': words})

def word_list_03(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        w = DeckOfCards[0]
        words = Word.objects.get(num = w[1])
    return render(request, '03.html', {'words': words})

def word_list_04(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        w = DeckOfCards[0]
        words = Word.objects.get(num = w[1])
    return render(request, '04.html', {'words': words})

def word_list_05(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        w = DeckOfCards[0]
        words = Word.objects.get(num = w[1])
    return render(request, '05.html', {'words': words})

def user_file_create(request):
    with open(r'cards/polzovatel/DeckOfCards.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)

    with open(r'cards/polzovatel/User01.txt', 'w') as f:
        json.dump(DeckOfCards, f)
    return render(request, 'new.html', {'DeckOfCards': DeckOfCards})

def user_training(request):
    with open(r'cards/polzovatel/User01.txt', 'r') as filehandle:
        DeckOfCards = json.load(filehandle)
        Word = DeckOfCards[0]

        if Word[0] == 0:
            Word[0] = 3
        elif Word[0] == 3:
            Word[0] = 7
        elif Word[0] == 7:
            Word[0] = 10
        elif Word[0] == 10:
            Word[0] = 10
        else:
            print('Ошибка статуса карты!')

        if Word[0] == 3:
            DeckOfCards.insert(3, Word), DeckOfCards.pop(0)
        elif Word[0] == 7:
            DeckOfCards.insert(7, Word), DeckOfCards.pop(0)
        elif Word[0] == 10:
            DeckOfCards.insert(10, Word), DeckOfCards.pop(0)
        else:
            print('Проверь перестановку карт!')

    with open(r'cards/polzovatel/User01.txt', 'w') as f:
        json.dump(DeckOfCards, f)
    return render(request, 'training.html', {'DeckOfCards': DeckOfCards})

def user_training_plus(request):
    pass

def user_training_minus(request):
    pass
