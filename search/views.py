from django.shortcuts import render
from board.models import Question
from django.db.models import Q
# Create your views here.


def searchResult(requset):
    if 'kw' in requset.GET:
        query = requset.GET.get('kw')
        items = Question.objects.all().filter(
            Q(subject__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    return render(requset, 'search.html', {'query':query, 'result':items})