from django.contrib import admin
from .models import Category, Product, ProductShade, ProductImage, Review, Order, OrderItem, ContactInquiry

class ProductShadeInline(admin.TabularInline):
    model = ProductShade
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'item_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'original_price', 'rating', 'in_stock', 'is_bestseller', 'is_new_arrival')
    list_filter = ('category', 'brand', 'in_stock', 'is_bestseller', 'is_new_arrival', 'is_featured')
    search_fields = ('name', 'brand', 'sku', 'description')
    inlines = [ProductShadeInline, ProductImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'product_name', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment', 'product_name')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'email', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'customer_name', 'email', 'phone')
    inlines = [OrderItemInline]

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
