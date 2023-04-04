from django.shortcuts import render, redirect
from item.models import Category, Item
from project.models import Project
from .models import FiringType
from django.db.models import Q
from core.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def search(request):
    query = request.GET.get('query', '')

    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        projects = Project.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query))

    return render(request, 'core/search.html', {
        'query':query,
        'items':items,
        'projects':projects,

    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'core/contact.html', context)


def index(request):
    #get the last 4 of the list
    items1 = Item.objects.filter(is_sold=False)
    items = items1[len(items1)-4:]
    categories = Category.objects.all()
    firingtype = FiringType.objects.all()
    projects1 = Project.objects.all()
    projects = projects1[len(projects1)-4:]
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'firingtype': firingtype,
        'projects': projects,
    })

