from django.shortcuts import render

# Create your views here.
def index_aplicaciongrupal(request):
    return render(request,"index.html")