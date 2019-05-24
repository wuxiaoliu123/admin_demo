from django.contrib import admin

# Register your models here.
#把创建的表进行注册
from .models import *
#添加一个django不打代码进行转义  不进行检测到的模块
from django.utils.safestring import mark_safe

class BookConfig(admin.ModelAdmin):

    def deletes(self):
        return mark_safe("<a href=''>删除</a>")
    list_display = ["title","publishDate","price","publish",deletes]#添加多个字段   在页面显示
    list_display_links = ["price"]#设置点击字段 可以进编辑页面进行编辑 也可以设置多个
    search_fields = ["title"] #搜索的框
    list_editable = ["title"] #可编辑的框
    #批量初始化
    def patch_init(self,request,queryset):
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"

    actions = [patch_init,]
    #可设置一个html页面代替django的后台页面
    # change_list_template = "list.html"



admin.site.register(Book,BookConfig)
print("1=======",admin.site._registry)
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)
print("2=======",admin.site._registry)

