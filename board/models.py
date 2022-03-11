from django.db import models




class Question(models.Model):

    subject = models.TextField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
# Create your models here.


class Answer(models.Model):

    answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_data = models.DateTimeField()