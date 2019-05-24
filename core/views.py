from django.shortcuts import render
from .models import Question

from django.views.generic import TemplateView
from .forms import UserRegistrationForm, FeedbackForm#, QuizForm

# # Create your views here.


class RegistrationPageView(TemplateView):
    def get(self, request):
        form = UserRegistrationForm()
        print("Empty User Registration Form...")
        print(form)

        return render(request, template_name='core/register.html', context={'form': form})

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        print("#####")
        print("Registration form with data...")
        print(form)
        print("#####")
        if form.is_valid():
            print("form is valid")
            user = form.save()

            print("#####")
            print("User __str__")
            print(user)

            print("#####")
            print("Registration form Raw POST request ")
            print(request.POST)

            user_dict = dict(form.data)
            del user_dict['csrfmiddlewaretoken']
            # saving the user dictionary to the session
            request.session['user_dict'] = user_dict
            print("#####")
            print("User dictionary saved in session without csrfmiddlewaretoken...")
            print(user_dict)

        else:
            print("form is invalid")
        return render(request, template_name='core/registration_submitted.html', context={'user': user})



class FeedbackView(TemplateView):
    def get(self, request):
        # form = FeedbackForm()
        ques = Question.objects.all()
        # request.session['ques'] = ques
        print("#####")
        print("Raw printing all the questions from the database as a Queryset... (it's basically a list")
        print("#####")
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
        data = request.POST
        print("#####")
        print("Printing the raw feedback POST request as a Querydict...")
        print(data)

        # retrieving the questions from the session
        # ques = request.session['ques']

        print("#####")
        ques = Question.objects.all()
        print("Printing the questions retrieved from the database as a Queryset...")
        print(ques)

        # retrieving the user from the session
        user_dict = request.session['user_dict']
        data_dict = dict(data)
        del data_dict['csrfmiddlewaretoken']

        print("#####")
        print("Printing the response data as a dictionary without csrf middleware token")
        print(data_dict)
        print("#####")

        response = {}
        response["Full Name"] = user_dict["full_name"][0]
        response["Email"] = user_dict["email"][0]

        qna_dict = {}
        for key in data_dict.keys():
            if key != 'csrfmiddlewaretoken':
                qna_dict[str(ques[int(key)-1])] = data_dict[key][0]

        response["Feedback"] = [qna_dict]
        print(response)

        import json
        response_json = json.dumps(response)
        print("#####")
        print("Converting the response dictionary into JSON string")
        print(response_json)
        # import ipdb;ipdb.set_trace()
        # if form.is_valid():
        #     response = form.save()
        #     print("form is valid")
        #     print(response)
        #
        # else:
        #     print("form is invalid")
        f = open("feedback_response.json", "w")
        f.write(response_json)
        f.close()
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
