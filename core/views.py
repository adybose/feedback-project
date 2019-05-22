from django.shortcuts import render
from .models import Question

from django.views.generic import TemplateView
from .forms import FeedbackForm#, QuizForm

# # Create your views here.


class FeedbackView(TemplateView):
    def get(self, request):
        # form = FeedbackForm()
        ques = Question.objects.all()
        return render(request, template_name='core/feedback.html', context={'ques': ques})
        # return render(request, template_name='core/feedback.html', context={'form': form, 'ques': ques})

    def post(self, request):
        # form = FeedbackForm(request.POST)
        data = request.POST
        data_dict = dict(data)
        print(data_dict)
        import json
        data_json = json.dumps(data_dict)
        print(data_json)
        # print(data)
        # if form.is_valid():
        #     response = form.save()
        #     print("form is valid")
        #     print(request.POST)
        #     print("#####################")
        #     print(response)
        #
        # else:
        #     print("form is invalid")
        return render(request, template_name='core/feedback_submitted.html', context={'data': data})
