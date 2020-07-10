from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    fullName = request.POST['fullName']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']

    context = {
        'name': fullName,
        'loc': location,
        'lang': language,
        'comm': comment,
    }
    return render(request, 'result.html', context)
