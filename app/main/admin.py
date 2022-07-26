from django.contrib import admin

# immport our community models for our tables in IRIS
from .models import (CommunityPost, CommunityComment, CommunityTag)

# register class which overrides default behaviour for model CommunityPost
@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
  # list of properties to show in table view
  list_display = ('posttype', 'name', 'publisheddate')
  # list of properties to show filter for on the right side of the tablee
  list_filter = ('posttype', 'lang', 'published')
  # default ordering, means from the latest date of PublishedDate
  ordering = ['-publisheddate', ]

@admin.register(CommunityComment)
class CommunityCommentAdmin(admin.ModelAdmin):
  # only this two fields show, (post is numeric by id in table post)
  list_display = ('post', 'created')
  # order by date of creation
  ordering = ['-created', ]

@admin.register(CommunityTag)
class CommunityTagAdmin(admin.ModelAdmin):
  # not so much to show
  list_display = ('name', )