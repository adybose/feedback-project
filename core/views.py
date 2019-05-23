from django.shortcuts import render
from .models import Question

from django.views.generic import TemplateView
from .forms import UserRegistrationForm, FeedbackForm#, QuizForm

# # Create your views here.


class RegistrationPageView(TemplateView):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, template_name='quiz/register.html', context={'form': form})

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            print("form is valid")
            print(request.POST)

        else:
            print("form is invalid")
        return render(request, template_name='quiz/registration_submitted.html', context={'user': user})



class FeedbackView(TemplateView):
    def get(self, request):
        # form = FeedbackForm()
        ques = Question.objects.all()
        print(ques)
        return render(request, template_name='core/feedback.html', context={'ques': ques})
        # return render(request, template_name='core/feedback.html', context={'form': form, 'ques': ques})

    def post(self, request):
        form = FeedbackForm(request.POST)

        data = request.POST
        data_dict = dict(data)
        print(data_dict)
        import json
        data_json = json.dumps(data_dict)
        print(data_json)

        if form.is_valid():
            response = form.save()
            print("form is valid")
            print(response)

        else:
            print("form is invalid")
        return render(request, template_name='core/feedback_submitted.html', context={'response': response})















# class MyTransictions(View):
#
#     @login_required()
#     def diposit_view(request):
#         if not request.user.is_authenticated:
#             raise Http404
#         else:
#             title = "Deposit"
#             form = DepositForm(request.POST or None)
#
#             if form.is_valid():
#                 deposit = form.save(commit=False)
#                 deposit.user = request.user
#                 deposit.user.balance += deposit.amount
#                 deposit.user.save()
#                 deposit.save()
#                 messages.success(request, 'You Have Deposited {} ₹.'
#                              .format(deposit.amount))
#                 return redirect("home")
#
#             context = {
#                     "title": title,
#                     "form": form
#                   }
#             return render(request, "transactions/form.html", context)
#
