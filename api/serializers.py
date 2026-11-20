from rest_framework import serializers
from .models import Category, Product, ProductShade, ProductImage, Review, Order, OrderItem, ContactInquiry

class CategorySerializer(serializers.ModelSerializer):
    itemCount = serializers.CharField(source='item_count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'itemCount']


class ProductShadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShade
        fields = ['name', 'hex']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    categorySlug = serializers.CharField(source='category.slug', read_only=True)
    shades = ProductShadeSerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField()
    
    # CamelCase aliases for seamless React integration
    originalPrice = serializers.DecimalField(source='original_price', max_digits=10, decimal_places=2, read_only=True)
    reviewsCount = serializers.IntegerField(source='reviews_count', read_only=True)
    isBestSeller = serializers.BooleanField(source='is_bestseller', read_only=True)
    isNewArrival = serializers.BooleanField(source='is_new_arrival', read_only=True)
    isFeatured = serializers.BooleanField(source='is_featured', read_only=True)
    shortDescription = serializers.CharField(source='short_description', read_only=True)
    howToUse = serializers.CharField(source='how_to_use', read_only=True)
    inStock = serializers.BooleanField(source='in_stock', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'brand',
            'category',
            'categorySlug',
            'price',
            'originalPrice',
            'original_price',
            'discount',
            'rating',
            'reviewsCount',
            'reviews_count',
            'isBestSeller',
            'is_bestseller',
            'isNewArrival',
            'is_new_arrival',
            'isFeatured',
            'is_featured',
            'sku',
            'inStock',
            'in_stock',
            'shortDescription',
            'short_description',
            'description',
            'benefits',
            'howToUse',
            'how_to_use',
            'ingredients',
            'image',
            'images',
            'shades',
        ]

    def get_images(self, obj):
        gallery = [img.image_url for img in obj.gallery_images.all()]
        if not gallery and obj.image:
            return [obj.image]
        return gallery or [obj.image]


class ReviewSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(source='product_name', required=False, allow_blank=True)

    class Meta:
        model = Review
        fields = ['id', 'name', 'role', 'rating', 'comment', 'productName', 'created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product_name')
    image = serializers.CharField(source='image_url', required=False, allow_blank=True)

    class Meta:
        model = OrderItem
        fields = ['name', 'shade', 'price', 'quantity', 'image']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    id = serializers.CharField(source='order_number', read_only=True)
    total = serializers.DecimalField(source='total_amount', max_digits=10, decimal_places=2)
    paymentMethod = serializers.CharField(source='payment_method')
    shippingAddress = serializers.CharField(source='shipping_address')
    customerName = serializers.CharField(source='customer_name')

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'customerName',
            'email',
            'phone',
            'shippingAddress',
            'subtotal',
            'discount',
            'shipping_fee',
            'total',
            'paymentMethod',
            'status',
            'created_at',
            'items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        # Auto generate order number if not provided
        import random
        order_number = f"GG-ORD-{random.randint(10000, 99999)}"
        validated_data['order_number'] = order_number

        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(
                order=order,
                product_name=item.get('product_name'),
                shade=item.get('shade', ''),
                price=item.get('price'),
                quantity=item.get('quantity', 1),
                image_url=item.get('image_url', '')
            )
        return order


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
