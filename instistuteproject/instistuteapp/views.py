from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()

def main_page(request):
    return render(request,'base.html')

def home_page(request):
    return render(request,'home_page.html')

def contact_page(request):
    return render(request,'contact_page.html')


def courese_page(request):
    return render(request,'courses_page.html')


def feedback_page(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1

            )
            data.save()
            fform=FeedbackForm()
            fdata=FeedbackData.objects.all()
            return  render(request,'feedback_page.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse('Invalid user data')

    else:
        fform=FeedbackForm()
        fdata=FeedbackData.objects.all()
        return render(request,'feedback_page.html',{'fform':fform,'fdata':fdata})












def ourteam_page(request):
    return render(request,'ourteam_page.html')


def gallery_page(request):
    return render(request,'gallery_page.html')