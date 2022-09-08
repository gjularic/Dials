from django.shortcuts import render


def index(request):
    """ View to return the index page """

    return render(request, 'home/index.html')


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
