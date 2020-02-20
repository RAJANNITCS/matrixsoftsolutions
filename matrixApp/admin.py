from django.contrib import admin
from matrixApp.models import Post, Comment


# -------------------Register admin --------------------------
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'body',
                    'Image', 'publish', 'created', 'updated', 'status']
    list_filter = ['status', 'author', 'created']
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ['status', 'publish']
    date_hierarchy = 'publish'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body',
                    'post', 'created', 'updated', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
# ----------xx---------Register admin --------------x------------


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
