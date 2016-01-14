from django.shortcuts import render
from .forms import SignupForm,ContactForm

# Create your views here.
def home(request):
    form=SignupForm(request.POST or None)
    if form.is_valid():
        instance=form.save()
    context={"form": form}

    return render(request, "base.html",context)

def contact(request):
    form=ContactForm
    context={"form":form}
    return render(request,"contact.html",context)
