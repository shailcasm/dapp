from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, 'common_app/index.html')

