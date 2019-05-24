from django.shortcuts import render
from .models import Question

from django.views.generic import TemplateView
from .forms import UserRegistrationForm, FeedbackForm#, QuizForm

# # Create your views here.


class RegistrationPageView(TemplateView):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, template_name='core/register.html', context={'form': form})

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            print(user)
            print(request.POST)
            user_dict = dict(form.data)
            del user_dict['csrfmiddlewaretoken']
            request.session['user_dict'] = user_dict

        else:
            print("form is invalid")
        return render(request, template_name='core/registration_submitted.html', context={'user': user})



class FeedbackView(TemplateView):
    def get(self, request):
        # form = FeedbackForm()
        ques = Question.objects.all()
        print("Printing all the questions from the database")
        print(ques)
        print("Printing all the questions with options on the console")
        print("##########")
        for que in ques:
            print(que.id)
            print(que.question)
            print(que.optiona)
            print(que.optionb)
            print(que.optionc)
            print(que.optiond)
            print("##########")

        return render(request, template_name='core/feedback.html', context={'ques': ques})
        # return render(request, template_name='core/feedback.html', context={'form': form, 'ques': ques})

    def post(self, request):
        form = FeedbackForm(request.POST)
        ques = Question.objects.all()
        user_dict = request.session['user_dict']
        data_dict = dict(form.data)
        response = {}
        response["Full Name"] = user_dict["full_name"][0]
        response["Email"] = user_dict["email"][0]

        for key in data_dict.keys():
            if key != 'csrfmiddlewaretoken':
                response[str(ques[int(key)-1])] = data_dict[key][0]

        print(response)
        # import json
        # data_json = json.dumps(data_dict)
        # print(data_json)
        # import ipdb;ipdb.set_trace()
        # if form.is_valid():
        #     response = form.save()
        #     print("form is valid")
        #     print(response)
        #
        # else:
        #     print("form is invalid")
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
