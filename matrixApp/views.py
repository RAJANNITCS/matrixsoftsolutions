from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from matrixApp.models import Post,Comment
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from matrixApp.forms import CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.


#------------------Index page view -----------------------
def index(request):
    post_list=Post.objects.all()
    my_list=[]
    for i in post_list:
        comments=i.comments.filter(active=True)
        comments=comments.count()
        my_list.append(comments)
       
    my_dic={i:my_list[i] for i in range(0,len(my_list))}   
    # print(my_dic)
    tag = Tag.objects.all()
    paginator=Paginator(post_list,6)
    page_number=request.GET.get('page')
    count=Post.objects.count()
    latest_posts=Post.objects.order_by('-publish')[:5]
    
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
        return redirect('/')
    return render(request,'HtmlFile/index.html',{'post_list':post_list,'tag':tag,'latest_posts':latest_posts,'count':count,'mydic':my_dic})
    

#--------x----------Index page view -----------x------------


#-----------------Post list view-----------------------------
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    my_list=[]
    for i in post_list:
        comments=i.comments.filter(active=True)
        comments=comments.count()
        my_list.append(comments)
       
    my_dic={i:my_list[i] for i in range(0,len(my_list))}   
    tag=None 
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    tag = Tag.objects.all()
    paginator=Paginator(post_list,6)
    page_number=request.GET.get('page')
    count=Post.objects.count()
    latest_posts=Post.objects.order_by('-publish')[:5]
    
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
    return render(request,'HtmlFile/post_list.html',{'post_list':post_list,'tag':tag,'latest_posts':latest_posts,'tag':tag,'count':count,'mydic':my_dic})
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
    post_list=Post.objects.all()
    my_list=[]
    for i in post_list:
        comments=i.comments.filter(active=True)
        comments=comments.count()
        my_list.append(comments)
       
    my_dic={i:my_list[i] for i in range(0,len(my_list))}   
    # print(my_dic)
    tag = Tag.objects.all()
    paginator=Paginator(post_list,6)
    page_number=request.GET.get('page')
    count=Post.objects.count()
    latest_posts=Post.objects.order_by('-publish')[:5]
    
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
        return redirect('/about')
    return render(request,'HtmlFile/about.html',{'post_list':post_list,'tag':tag,'latest_posts':latest_posts,'count':count,'mydic':my_dic})
   
#---------x---------About us--------------------x-----------


#----------------------Downloads------------------------------
def Download(request):
    post_list=Post.objects.all()
    my_list=[]
    for i in post_list:
        comments=i.comments.filter(active=True)
        comments=comments.count()
        my_list.append(comments)
       
    my_dic={i:my_list[i] for i in range(0,len(my_list))}   
    # print(my_dic)
    tag = Tag.objects.all()
    paginator=Paginator(post_list,6)
    page_number=request.GET.get('page')
    count=Post.objects.count()
    latest_posts=Post.objects.order_by('-publish')[:5]
    
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
        return redirect('/download')
    return render(request,'HtmlFile/download.html',{'post_list':post_list,'tag':tag,'latest_posts':latest_posts,'count':count,'mydic':my_dic})
#----------x------------Downloads----------------x--------------