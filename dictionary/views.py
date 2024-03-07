from django.shortcuts import render, redirect
from PyDictionary import PyDictionary

# Create your views here.


def search(request):
    return render(request,'index.html')

def get_meaning(request):
    meaning = None
    if request.method == 'POST':
        word = request.POST.get('search')
        dictionary=PyDictionary()
        meaning = dictionary.meaning(word)

    context = {
        'word' : word,
        'meaning' : meaning
    }    
        
    return render(request,'word.html', context=context)
    
    


