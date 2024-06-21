from django.shortcuts import render

# Create your views here.
def gallery(request):
    context = {}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    context = {}
    return render(request, 'photos/photos.html', context)

def addPhoto(request):
    context = {}
    return render(request, 'photos/add.html', context)