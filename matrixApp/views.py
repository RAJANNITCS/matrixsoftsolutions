from django.shortcuts import render
from matrixApp.models import Post
# Create your views here.


#------------------Index page view -----------------------
def index(request):
    return render(request,'HtmlFile/index.html')

#--------x----------Index page view -----------x------------


#-----------------Post list view-----------------------------
def post_list_view(request):
    post_list=Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list})
#--------x---------Post list view----------------x-------------