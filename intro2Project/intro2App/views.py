from django.http import HttpResponse

# Function for the default request
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

# Function for "music" request
def music(request):
    return HttpResponse("Jimmy_Hendrix , Elton_John, Michael_Jackson")

# Function for the first artist
def Jimmy_Hendrix(request):
    return HttpResponse("The best with his guitar.")

# Function for the second artist
def Elton_John(request):
    return HttpResponse("Mister piano man.")

# Function for the third artist
def Michael_Jackson(request):
    return HttpResponse("The king of pop.")