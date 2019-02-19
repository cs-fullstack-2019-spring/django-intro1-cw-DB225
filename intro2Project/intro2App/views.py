from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def music(request):
    return HttpResponse("Jimmy_Hendrix , Elton_John, Michael_Jackson")

def Jimmy_Hendrix(request):
    return HttpResponse("The best with his guitar.")

def Elton_John(request):
    return HttpResponse("Mister piano man.")

def Michael_Jackson(request):
    return HttpResponse("The king of pop.")