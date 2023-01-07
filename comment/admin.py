
from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_time', 'validated_by', 'parent_comment', 'status')
    list_filter = ('validated_by', 'status')
    search_fields = ('user',)


admin.site.register(HotelComment, CommentAdmin)
admin.site.register(HotelRoomComment, CommentAdmin)
admin.site.register(ResidentialComment, CommentAdmin)
admin.site.register(AirLineComment, CommentAdmin)
admin.site.register(AirPortComment, CommentAdmin)
