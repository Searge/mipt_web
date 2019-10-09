from django.http import HttpResponse
from django.views.decorators import http, csrf


@csrf_exempt
@require_GET
def simple_route(request):
    try:
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=405)


def sum_route(request, a, b):
    try:
        return HttpResponse(str(int(a) + int(b)))
    except:
        return HttpResponse(status=404)


def slug_route(request, slug):
    try:
        return HttpResponse(slug)
    except:
        return HttpResponse(status=404)


@require_GET
def sum_get_method(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    try:
        return HttpResponse(str(int(a)+int(b)))
    except:
        return HttpResponse(status=400)


@require_POST
@csrf_exempt
def sum_post_method(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    try:
        return HttpResponse(str(int(a)+int(b)))
    except:
        return HttpResponse(status=400)
