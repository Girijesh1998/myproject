from django.shortcuts import render

# Create your views here.
def project(request):
    context = {'project': 'active'}
    return render(request, 'project/myproject.html', context)

def project1(request):
    context = {'project1': 'active'}
    return render(request, 'project/myproject_1.html', context)