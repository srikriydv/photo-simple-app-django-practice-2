from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import addPhotoForm

# Create your views here.
def gallery(request):
    category_id = request.GET.get('q')
    if category_id:
        photos = Photo.objects.filter(category_id=category_id)
    else:
        photos = Photo.objects.all()

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
