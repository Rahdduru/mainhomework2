from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') #render:세개의 인자를 받을 수 있음(두개는 필수 세번째는 선택적으로 받음(사전형 객체))

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})