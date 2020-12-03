from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def jobs_home(request):
    jobs = Articles.objects.order_by('-published_date')
    return render(request, 'jobs/jobs_home.html', {'jobs': jobs})

class JobsDetailView(DetailView):
    model = Articles
    template_name = 'jobs/details_view.html'
    context_object_name = 'article'

class JobsUpdateView(UpdateView):
    model = Articles
    template_name = 'jobs/create.html'
    
    form_class = ArticlesForm

class JobsDeleteView(DeleteView):
    model = Articles
    success_url = '/jobs/'
    template_name = 'jobs/delete.html'
    

def create(request):
    error = ''  
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заповнена неправильно'    

    form = ArticlesForm()

    data={
        'form': form,
        'error': error
    }

    return render(request, 'jobs/create.html', data)
