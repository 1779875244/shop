from django.contrib import admin
from .models import Category,Product
# Register your models here.

admin.site.site_header='商城管理'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug','price',
                    'stock','active','created',
                    'updated','isDelete')
    list_filter = ('active','created','updated')
    prepopulated_fields = {'slug':('name',)}