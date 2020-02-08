from django.contrib import admin
from matrixApp.models import Post


#-------------------Register admin --------------------------
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','slug','author','body','Image','publish','created','updated','status']
    list_filter=['status','author','created']
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    ordering=['status','publish']
    date_hierarchy='publish'
    
#----------xx---------Register admin --------------x------------


admin.site.register(Post,PostAdmin)