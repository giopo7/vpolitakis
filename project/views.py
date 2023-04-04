from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.db.models import Q

# Create your views here.

def projects(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    projects = Project.objects.all()

    if category_id:
        projects = projects.filter(category_id=category_id)

    if query:
        projects = projects.filter(Q(name__icontains=query) | Q(collab__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query))

    return render(request, 'project/projects.html',{
        'projects': projects,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    similar = Project.objects.filter(category=project.category).exclude(pk=pk)[0:4]
    # filter(category=item.category)

    return render(request, 'project/detail.html', {
        'project': project,
        'similar': similar,
    })