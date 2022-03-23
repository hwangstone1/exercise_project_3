from django.shortcuts import render
from board.models import Question
# Create your views here.


def main(request):

    question_list = Question.objects.order_by('-create_date')[:5]



    return render(request, 'apple/apple.html', {'question_list' : question_list})