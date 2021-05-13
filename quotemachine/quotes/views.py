from django.shortcuts import render
from .models    import *
from .forms     import *
# Create your views here.
def create_quote_view(request):
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        print("saved")
    else:
        print("failed to save")
    
    context = {
        'form': form
    }
    return render(request, "quotes/quote_create.html", context)