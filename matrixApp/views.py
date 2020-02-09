from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from matrixApp.models import Post
from django.core.mail import EmailMessage
from matrixApp.forms import CommentForm
from taggit.models import Tag

# Create your views here.


#------------------Index page view -----------------------
def index(request):
    return render(request,'HtmlFile/index.html')

#--------x----------Index page view -----------x------------


#-----------------Post list view-----------------------------
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None 
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,4)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    if request.method=="POST":
        mailid = request.POST['mailid']
        subject='thanks notes'
        massage='thanks for visiting our website'
        send_mail(subject,massage,'www.matrixsoftsolutions.com',[mailid])
        return redirect('/post_list')
    return render(request,'HtmlFile/post_list.html',{'post_list':post_list,'tag':tag})
#--------x---------Post list view----------------x-------------

#---------------------Post detail view------------------------
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'HtmlFile/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
#----------x-----------Post detail view--------------x----------

#------------------About us-------------------------------
def about(request):
    return render(request,'HtmlFile/about.html')
#---------x---------About us--------------------x-----------


#----------------------Downloads------------------------------
def Download(request):
    return render(request,'HtmlFile/download.html')
#----------x------------Downloads----------------x--------------