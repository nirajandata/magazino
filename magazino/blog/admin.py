from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    # summernote_fields='__all__'
    summernote_fields = ('content',)

#halko customize gardeko ni , heheheh

# class PostAdmin(admin.ModelAdmin ):
# 	list_display=('title','slug','status','created_on')
# 	list_filter=("status",)
# 	search_fields=['title','content']
# 	prepopulated_fields={'slug':("title",)}

admin.site.register(Post,PostAdmin)