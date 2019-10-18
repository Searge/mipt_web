from django.shortcuts import render

from django.views import View


class FormDummyView(View):

    def get(self, request):
        hello = request.GET.get('hello')
        return render(request, 'form.html', {'hello': hello})
