from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'accounts/index.html')