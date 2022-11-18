from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    form=ContactForm()
    dict_form={'form':form}
    return render(request,'contact.html',dict_form)
def creation(request):
    return render(request,'creation.html')
