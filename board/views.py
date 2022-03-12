from django.shortcuts import render, get_object_or_404,redirect
from .models import Question
from django.utils import timezone
# Create your views here.


def index(request):

    question_list = Question.objects.order_by('create_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id) # id가 question_id 인 target 을 가져온다.
    context = {'question' : question}
    return render(request, 'board/question_detail.html', context)


def answer_create(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    return redirect('board:detail', question_id=question.id)
