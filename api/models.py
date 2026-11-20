from django.db import models

class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=500, blank=True)
    item_count = models.CharField(max_length=50, blank=True, default='0 Products')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(default=0, help_text="Discount percentage")
    rating = models.FloatField(default=4.8)
    reviews_count = models.IntegerField(default=0)
    is_bestseller = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    sku = models.CharField(max_length=50, unique=True)
    in_stock = models.BooleanField(default=True)
    short_description = models.TextField(blank=True)
    description = models.TextField()
    benefits = models.JSONField(default=list, blank=True, help_text="List of benefit bullets")
    how_to_use = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    image = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} - {self.name}"


class ProductShade(models.Model):
    product = models.ForeignKey(Product, related_name='shades', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=20, help_text="Color hex code, e.g. #B86561")

    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='gallery_images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} Image {self.order}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150, default='Verified Buyer')
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    product_name = models.CharField(max_length=200, blank=True)
    product = models.ForeignKey(Product, related_name='reviews', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.rating}★)"


class Order(models.Model):
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    shipping_address = models.TextField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='UPI')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.order_number} ({self.customer_name})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    shade = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.product_name} in {self.order.order_number}"


class ContactInquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact Inquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"
