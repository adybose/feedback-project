from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Question


class FeedbackForm(ModelForm):

    class Meta:
        model = Question
        fields = ["question",
                  "optiona",
                  "optionb",
                  "optionc",
                  "optiond",
        ]

    # def save(self, commit=True):
    #     response = super(ModelForm, self).save(commit=False)
    #     if commit:
    #         response.save()
    #     print(response)
    #     return response
