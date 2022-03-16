from django.shortcuts import render
from board.models import Question
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def searchResult(request):

    page = request.GET.get('page', '1')

    if 'kw' in request.GET:
        query = request.GET.get('kw')
        items = Question.objects.all().filter(
            Q(subject__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    pagenator = Paginator(items, 10)
    page_obj = pagenator.get_page(page)

    return render(request, 'search.html', {'query':query, 'result':page_obj})