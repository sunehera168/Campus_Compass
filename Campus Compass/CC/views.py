from django.shortcuts import render, get_object_or_404
from .models import *
from CC.models import InstituteInfo  # Correct import
# Create your views here.
def Home(request):
    return render(request,template_name='CC\Home.html')

def Login(request):
    return render(request,template_name='CC\Login.html')

def HomeOverview(request):
    university_category = Category.objects.get(name="University")
    InstituteName = InstituteInfo.objects.filter(category=university_category).prefetch_related('images')
    context = {'InstituteName': InstituteName}
    return render(request, 'CC/HomeOverview.html', context)

from django.shortcuts import render, get_object_or_404
from .models import InstituteInfo  # Replace with your actual model name

def institute_detail(request, institute_id):
    institute = get_object_or_404(InstituteInfo, pk=institute_id)  # Correct model
    return render(request, 'CC/institute_detail.html', {'institute': institute})

def Colleges(request):
    college_category = Category.objects.get(name="College")
    InstituteName = InstituteInfo.objects.filter(category= college_category).prefetch_related('images')
    context = {'InstituteName': InstituteName}
    return render(request, 'CC/Colleges.html', context)    