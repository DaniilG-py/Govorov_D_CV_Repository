from django.shortcuts import render
from django.views.generic import View

from .models import WorkingExperience, EducationExperience


class BaseView(View):

    def get(self, request, *args, **kwargs):
        work_exp = WorkingExperience.objects.all()
        educ_exp = EducationExperience.objects.all()
        context = {
                'work_exp': work_exp,
                'educ_exp': educ_exp,
            }
        return render(request, 'index.html', context)
