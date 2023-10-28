# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Register
# Create your views here.
def homepage(request):
    return render(request,'Homepage.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        register = Register(name=name, address=address, contact=contact,email=email)
        register.save()
    return render(request,'register.html')

def questions(request):
    return render(request,'Questions.html')
# def result(request):
#     return render(request,'result.html')


# def questions(request):
#     if request.method == 'POST':
#         total_score = 0
#         correct_answers = {
#             'answer1': 'B',
#             'answer2': 'B',
#             'answer3': 'C',
#             'answer4': 'B',
#             'answer5': 'C',
#             'answer6': 'C',
#             'answer7': 'D',
#             'answer8': 'A',
#             'answer9': 'A',
#             'answer10': 'B',
#         }

#         for i in range(1, 11):
#             selected_answer = request.POST.get(f'answer{i}')
#             if selected_answer == correct_answers[f'answer{i}']:
#                 total_score += 10

#         return redirect('result', total_score=total_score)

#     return render(request, 'questions.html')

# def result(request, total_score):
#     return render(request, 'result.html', {'total_score': total_score})



