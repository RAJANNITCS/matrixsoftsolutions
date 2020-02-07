from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from matrixApp.models import Post
# Create your views here.


#------------------Index page view -----------------------
def index(request):
    return render(request,'HtmlFile/index.html')

#--------x----------Index page view -----------x------------


#-----------------Post list view-----------------------------
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'HtmlFile/post_list.html',{'post_list':post_list})
#--------x---------Post list view----------------x-------------

#---------------------Post detail view------------------------
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'HtmlFile/post_detail.html',{'post':post})
#----------x-----------Post detail view--------------x----------

#------------------About us-------------------------------
def about(request):
    return render(request,'HtmlFile/about.html')
#---------x---------About us--------------------x-----------


#----------------------Downloads------------------------------
def Download(request):
    return render(request,'HtmlFile/download.html')
#----------x------------Downloads----------------x--------------