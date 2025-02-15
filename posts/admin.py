from django.contrib import admin
from .models import Post,PostFile,Comment,Like
# Register your models here.

class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ['file']
    extra = 0
    can_delete = False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active','is_public','created_time']
    list_filter = ['is_active','is_public']
    search_fields = ['title']
    inlines = (PostFileInlineAdmin,)
    
    def has_change_permission(self, request, obj = ...):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False
    
    def has_add_permission(self, request):
        return False 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','is_enable','created_time','updated_time']
    list_filter = ['user','post','is_enable']
    search_fields = ['content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','is_like','created_time','updated_time']
    search_fields = ['user','post','is_like']
