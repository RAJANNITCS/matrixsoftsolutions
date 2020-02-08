from django.db import models
#--------------athonticaton user----------
from django.contrib.auth.models import User
#--------------time zone--------------------
from django.utils import timezone

#---------------redairect---------------
from django.urls import reverse

#-----------------model manager (custome manager)---------
class CustomeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


#-------------------Post classes-------------------
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.PROTECT)
    body=models.TextField()
    Image=models.ImageField(upload_to='images/')
    publish=models.DateField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    
    objects=CustomeManager()
    
    class Meta:
        ordering=('-publish',)
        
    def __str__(self):
        return self.title
    
#----------Page redirect on detatie page------------------
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
    
#--------X-----------Post classes----------X---------