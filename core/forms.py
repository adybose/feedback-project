from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Response


class UserRegistrationForm(ModelForm):

    class Meta:
        model = User
        fields = ["full_name",
                  "email",
                  ]

    def save(self, commit=True):
        user = super(ModelForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user


class FeedbackForm(ModelForm):

    class Meta:
        model = Response
        fields = ["question",
                  "answer",
                  "user",
        ]

    def save(self, commit=True):
        response = super(ModelForm, self).save(commit=False)
        response.question = self.cleaned_data['question']
        response.answer = self.cleaned_data['answer']
        response.user = self.cleaned_data['user']
        if commit:
            response.save()
        return response
