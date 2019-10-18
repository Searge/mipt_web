import json
from .forms import DummyForm
from .schemas import REVIEW_SCHEMA
from django.shortcuts import render
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError


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


class SchemaView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponcse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponcse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError:
            pass
