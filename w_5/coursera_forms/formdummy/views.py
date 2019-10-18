from django.shortcuts import render
from django.views import View
from .forms import DummyForm


class FormDummyView(View):

    def get(self, request):
        form = DummyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        text = request.POST.get('text')
        grade = request.POST.get('grade')
        image = request.FILES.get('image')
        content = image.read()
        context = {
            'text': text,
            'grade': grade,
            'content': content
        }
        return render(request, 'form.html', context)
