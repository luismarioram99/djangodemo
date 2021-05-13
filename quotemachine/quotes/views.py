from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models    import *
from .forms     import *
# Create your views here.
@login_required
def create_quote_view(request, *LoginRequiredMixin):
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