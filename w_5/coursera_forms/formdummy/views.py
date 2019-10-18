from django.shortcuts import render
from django.views import View
from .forms import DummyForm


class FormDummyView(View):

    def get(self, request):
        form = DummyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = DummyForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context)
        else:
            return render(request, 'error.html', {'error': form.errors})
