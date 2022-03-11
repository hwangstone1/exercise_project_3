from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.


def index(request):

    question_list = Question.objects.order_by('create_date')
    context = {'question_list': question_list}
    return render(request, 'board/board.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id) # id가 question_id 인 target 을 가져온다.
    context = {'question' : question}
    return render(request, 'board/detail.html', context)

