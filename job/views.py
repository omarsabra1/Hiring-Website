from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job,Category
from django.core.paginator import Paginator
from django.shortcuts import redirect,reverse
from .form import ApplyForm,AddForm
from .filters import JobFilter
# Create your views here.
def job_list(request):
    job_list=Job.objects.all()
    category=Category.objects.all()
    #filters
    my_filter=JobFilter(request.GET,queryset=job_list)
    job_list=my_filter.qs


    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj,'myfilter':my_filter,'category':category}
    return render(request,'job\job_List.html',context)

def job_detail(request,slug):

    job_detail=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        print("I can POST")
        if form.is_valid:
            my_form=form.save(commit=False)
            my_form.job=job_detail
            my_form.save()
    else:
        form=ApplyForm()
    context={'job':job_detail,'form':form}
    return render(request,'job\job_Details.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form=AddForm(request.POST,request.FILES)
        if form.is_valid:
            job_form=form.save(commit=False)
            job_form.owner=request.user
            job_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
            form=AddForm()
    context={'add':form}
    return render(request,'job/add_job.html',context)
