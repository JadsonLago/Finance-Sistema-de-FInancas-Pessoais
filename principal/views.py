from django.shortcuts import render

# Create your views here.
def home(request):
    message = 'Hello World'
    context = {'message': message}
    return render(request, 'principal/home.html', context)
