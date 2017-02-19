from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {"courses":courses})

def submit(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST["name"], description=request.POST["description"])
        print Course.objects.all()
        return redirect('/')
    elif request.method == 'GET':
        return redirect('/')

def delete(request, id):
    # query for deleteion
    target = Course.objects.get(id=id)
    return render(request, 'course/delete.html', {"target":target})

def destroy(request, id):
    if request.method == 'POST':
        Course.objects.filter(id=id).delete()
    return redirect('/')

def comments(request, id):
    try:
        target = Course.objects.get(id=id)
    except Course.DoesNotExist:
        messages.add_message(request, messaes.INFO, "Course not found!")
        return redirect('/')
    return render(request, 'course/comment.html', {"target":target})
