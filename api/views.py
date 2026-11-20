from rest_framework import viewsets, generics, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Category, Product, Review, Order, ContactInquiry
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    OrderSerializer,
    ContactInquirySerializer
)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list and retrieve luxury makeup categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for browsing products with full filtering, sorting, and search.
    """
    queryset = Product.objects.all().select_related('category').prefetch_related('shades', 'gallery_images')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'brand', 'short_description', 'description', 'category__name']
    ordering_fields = ['price', 'rating', 'created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        # Filter by category slug or id
        category = params.get('category')
        if category and category.lower() != 'all':
            queryset = queryset.filter(
                Q(category__slug__iexact=category) | Q(category__id__iexact=category)
            )

        # Filter by brand
        brand = params.get('brand')
        if brand and brand.lower() != 'all':
            queryset = queryset.filter(brand__iexact=brand)

        # Price filters
        min_price = params.get('min_price') or params.get('minPrice')
        if min_price:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                pass

        max_price = params.get('max_price') or params.get('maxPrice')
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass

        # Rating filter
        rating = params.get('rating')
        if rating:
            try:
                queryset = queryset.filter(rating__gte=float(rating))
            except ValueError:
                pass

        # Best sellers filter
        filter_type = params.get('filter')
        if filter_type == 'bestsellers':
            queryset = queryset.filter(is_bestseller=True)
        elif filter_type == 'new':
            queryset = queryset.filter(is_new_arrival=True)
        elif filter_type == 'featured':
            queryset = queryset.filter(is_featured=True)

        return queryset

    @action(detail=False, methods=['get'])
    def bestsellers(self, request):
        qs = self.get_queryset().filter(is_bestseller=True)[:8]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def new_arrivals(self, request):
        qs = self.get_queryset().filter(is_new_arrival=True)[:8]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint for verified customer reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint to place, track, and view customer orders.
    """
    queryset = Order.objects.all().prefetch_related('items')
    serializer_class = OrderSerializer
    lookup_field = 'order_number'

    def get_queryset(self):
        qs = super().get_queryset()
        email = self.request.query_params.get('email')
        if email:
            qs = qs.filter(email__iexact=email)
        return qs


class ContactInquiryCreateView(generics.CreateAPIView):
    """
    API endpoint for customer concierge contact form submissions.
    """
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
