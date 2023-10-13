from django.shortcuts import render, redirect, get_object_or_404
from .models import Keyword, Trend
from .forms import KeywordForm

def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    keywords = Keyword.objects.all()
    context = {
        'form': form,
        'keywords':keywords,
    }
    return render(request,'trends/keyword.html', context)


def keyword_detail(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling():
    pass

def crawling_histogram():
    pass

def crawling_advanced():
    pass

# Create your views here.
