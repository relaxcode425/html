from django.shortcuts import render

# Create your views here.
def Principal(request):
    context={}
    return render(request, 'pages/Principal.html', context)