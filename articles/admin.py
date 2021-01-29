from django.contrib import admin
from .models import Article, Comment

'''
##eSTO ES UNA FORMA
# Para ver de forma copada la relacion comentario y artiuclo
class CommentInline(admin.StackedInline):  # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
'''

# eSTA ES OTRA


class CommentInline(admin.TabularInline):  # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
