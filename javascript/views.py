from django.shortcuts import render

# Create your views here.
def javascript_home(request):
    return render(request, 'home/javascript-home.html')


def javascript_beginner(request):
    return render(request, 'home/javascript-beginner.html')


def javascript_node(request):
    return render(request, 'home/javascript-node.html')


def javascript_react(request):
    return render(request, 'home/javascript-react.html')