from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("欢迎使用")
    name = "胡歌"
    return render(request, 'main.html', {'n1':name})
