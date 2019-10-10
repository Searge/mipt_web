from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def echo(request):
    res = request.META.get('HTTP_X_PRINT_STATEMENT', 'empty')
    if request.method == 'GET':
        params = request.GET
    elif request.method == 'POST':
        params = request.POST
    else:
        params = {}

    return render(request, 'echo.html',
                  context={
                      'method': request.method.lower(),
                      'res': res,
                      'params': params
                  })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
