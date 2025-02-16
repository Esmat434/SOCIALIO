from django.contrib import admin
from .models import Friendship
# Register your models here.

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['id','request_from','request_to','is_accepted','created_time']
    list_filter = ['request_from','request_to','is_accepted']
    actions = False

    # def has_add_permission(self, request):
    #     return False
    # def has_change_permission(self, request, obj = ...):
    #     return False
    def has_delete_permission(self, request, obj = ...):
        return False