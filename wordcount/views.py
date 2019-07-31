from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'count/main.html')


def about(request):
    return render(request, 'count/about.html')


def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # 증가
            word_dictionary[word] += 1
        else:
            # 딕셔너리 추가
            word_dictionary[word] = 1
    return render(request, 'count/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
