
from django.db import models
from django.core.validators import RegexValidator

from django import forms

# Create your models here.

NAME_REGEX = '^[a-zA-Z ]*$'

# Create your models here.


class User(models.Model):
    full_name = None
    email = None

    full_name = models.CharField(
        max_length=256,
        blank=False,
        validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ]
        )
    email = models.EmailField(blank=False)

    def __str__(self):
        return str(self.full_name)


class Question(models.Model):
    question = models.CharField(max_length=250)
    optiona = models.CharField(max_length=100)
    optionb = models.CharField(max_length=100)
    optionc = models.CharField(max_length=100)
    optiond = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer
