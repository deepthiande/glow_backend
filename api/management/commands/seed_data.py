from django.core.management.base import BaseCommand
from api.models import Category, Product, ProductShade, ProductImage, Review

class Command(BaseCommand):
    help = 'Seeds initial realistic makeup categories, products, and reviews into the database'

    def handle(self, *args, **options):
        self.stdout.write("Seeding GLOW & GLAM initial beauty catalog...")

        # 1. Categories
        categories_data = [
            {
                'id': 'lipsticks',
                'name': 'Lipsticks',
                'slug': 'lipsticks',
                'description': 'Velvet mattes, hydrating satins & glassy tints',
                'image': 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80',
                'item_count': '18 Products'
            },
            {
                'id': 'face-makeup',
                'name': 'Face Makeup',
                'slug': 'face-makeup',
                'description': 'Flawless foundations, skin-blurring concealers & powders',
                'image': 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80',
                'item_count': '24 Products'
            },
            {
                'id': 'eye-makeup',
                'name': 'Eye Makeup',
                'slug': 'eye-makeup',
                'description': 'Celestial eyeshadows, waterproof liners & fluttery mascaras',
                'image': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=800&q=80',
                'item_count': '16 Products'
            },
            {
                'id': 'blush-glow',
                'name': 'Blush & Glow',
                'slug': 'blush-glow',
                'description': 'Dewy liquid blushes, baked highlighters & sunlit bronzers',
                'image': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=800&q=80',
                'item_count': '14 Products'
            },
            {
                'id': 'brushes-tools',
                'name': 'Brushes & Tools',
                'slug': 'brushes-tools',
                'description': 'Ultra-soft vegan bristles & ergonomic beauty blenders',
                'image': 'https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?auto=format&fit=crop&w=800&q=80',
                'item_count': '12 Products'
            },
            {
                'id': 'skincare',
                'name': 'Skincare',
                'slug': 'skincare',
                'description': 'Nourishing serums, prep mists & barrier renewal balms',
                'image': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80',
                'item_count': '15 Products'
            }
        ]

        cat_objs = {}
        for c_data in categories_data:
            cat, created = Category.objects.update_or_create(
                id=c_data['id'],
                defaults=c_data
            )
            cat_objs[cat.id] = cat
            status_text = "Created" if created else "Updated"
            self.stdout.write(f"  [Category] {status_text} {cat.name}")

        # 2. Products Data
        products_data = [
            {
                'id': 'gg-lip-01',
                'name': 'Velvet Petal Weightless Matte Lipstick',
                'brand': 'GLOW & GLAM Atelier',
                'category_id': 'lipsticks',
                'price': 1399.00,
                'original_price': 1799.00,
                'discount': 22,
                'rating': 4.9,
                'reviews_count': 384,
                'is_bestseller': True,
                'is_new_arrival': False,
                'is_featured': True,
                'sku': 'GG-LIP-001',
                'in_stock': True,
                'short_description': 'Infused with French camellia oil for a cashmere-soft matte finish that never feathers.',
                'description': 'Crafted with micronized pigments and enriched with nourishing wild rosehip and camellia oil, Velvet Petal delivers intense, weightless color in a single swipe.',
                'benefits': [
                    '12-hour weightless matte wear',
                    'Infused with Camellia Oil & Hyaluronic spheres',
                    'Non-drying, blur-filter effect',
                    '100% Vegan & Cruelty-Free'
                ],
                'how_to_use': 'Glide directly across the lips starting from the cupid’s bow outwards.',
                'ingredients': 'Dimethicone, Camellia Japonica Seed Oil, Rosa Canina (Rosehip) Fruit Oil, Hyaluronic Acid Spheres, Tocopheryl Acetate.',
                'image': 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80',
                    'https://images.unsplash.com/photo-1625093742435-6fa192b6fb10?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Rose Cashmere', 'hex': '#B86561'},
                    {'name': 'Toasted Nude', 'hex': '#A86D58'},
                    {'name': 'Berry Soufflé', 'hex': '#873447'},
                    {'name': 'Spiced Terracotta', 'hex': '#B04C3E'}
                ]
            },
            {
                'id': 'gg-face-02',
                'name': 'Luminous Silk Hydrating Foundation',
                'brand': 'GLOW & GLAM Privé',
                'category_id': 'face-makeup',
                'price': 2499.00,
                'original_price': 2999.00,
                'discount': 16,
                'rating': 4.8,
                'reviews_count': 512,
                'is_bestseller': True,
                'is_new_arrival': False,
                'is_featured': True,
                'sku': 'GG-FCE-002',
                'in_stock': True,
                'short_description': 'Buildable medium-to-full coverage with a natural lit-from-within radiance.',
                'description': 'Inspired by fine silk charmeuse, this revolutionary liquid foundation unifies skin tone with light-reflecting micro-pearls and Botanical Squalane.',
                'benefits': [
                    'Second-skin luminous finish',
                    'Medium buildable coverage',
                    'Enriched with 4% Niacinamide & Squalane'
                ],
                'how_to_use': 'Dispense 1-2 pumps onto the back of your hand. Buff into skin with a brush or damp sponge.',
                'ingredients': 'Aqua/Water, Squalane, Niacinamide, Glycerin, Titanium Dioxide, Dimethicone.',
                'image': 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Fair Ivory (10N)', 'hex': '#F3E4D6'},
                    {'name': 'Warm Beige (20W)', 'hex': '#E6C9B0'},
                    {'name': 'Golden Honey (30W)', 'hex': '#D2A782'}
                ]
            },
            {
                'id': 'gg-blush-03',
                'name': 'Dew Bloom Liquid Radiant Blush',
                'brand': 'Aura Glow',
                'category_id': 'blush-glow',
                'price': 1199.00,
                'original_price': 1499.00,
                'discount': 20,
                'rating': 4.9,
                'reviews_count': 620,
                'is_bestseller': True,
                'is_new_arrival': False,
                'is_featured': True,
                'sku': 'GG-BLS-003',
                'in_stock': True,
                'short_description': 'Weightless liquid blush that melts effortlessly into cheeks for an all-day pinch of glow.',
                'description': 'An airy, serum-like cheek tint that melts effortlessly into skin, creating a seamless, healthy flush.',
                'benefits': [
                    'Weightless serum formula',
                    'Infused with White Lily & Lotus extract'
                ],
                'how_to_use': 'Dab 1-2 dots onto cheekbones and blend upwards.',
                'ingredients': 'Isododecane, White Water Lily Extract, Nelumbo Nucifera Extract, Mica.',
                'image': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Soft Peony', 'hex': '#DE7F8F'},
                    {'name': 'Apricot Sunset', 'hex': '#E78C6E'},
                    {'name': 'Warm Terracotta', 'hex': '#BA594C'}
                ]
            },
            {
                'id': 'gg-eye-04',
                'name': 'Celestial Nights 12-Pan Eyeshadow Palette',
                'brand': 'GLOW & GLAM Atelier',
                'category_id': 'eye-makeup',
                'price': 2799.00,
                'original_price': 3499.00,
                'discount': 20,
                'rating': 4.9,
                'reviews_count': 295,
                'is_bestseller': True,
                'is_new_arrival': False,
                'is_featured': True,
                'sku': 'GG-EYE-004',
                'in_stock': True,
                'short_description': '12 buttery velvet mattes, multidimensional foiled metallics, and diamond toppers.',
                'description': 'A curated wardrobe of 12 celestial eyeshadows ranging from cashmere neutrals to gilded metallics.',
                'benefits': ['12 curated shades', 'Intense one-swipe payoff', 'Zero chalkiness'],
                'how_to_use': 'Apply matte shades into the crease and pat metallic shades onto the lid.',
                'ingredients': 'Talc, Synthetic Fluorphlogopite, Mica, Dimethicone, Zinc Stearate.',
                'image': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Champagne Dream', 'hex': '#F0E2CD'},
                    {'name': 'Rose Quartz', 'hex': '#D6A99D'},
                    {'name': 'Molten Bronze', 'hex': '#9B613A'}
                ]
            },
            {
                'id': 'gg-lip-05',
                'name': 'Glace Lip Glaze High-Shine Oil',
                'brand': 'Maison de Beauté',
                'category_id': 'lipsticks',
                'price': 999.00,
                'original_price': 1299.00,
                'discount': 23,
                'rating': 4.7,
                'reviews_count': 418,
                'is_bestseller': False,
                'is_new_arrival': True,
                'is_featured': True,
                'sku': 'GG-LIP-005',
                'in_stock': True,
                'short_description': 'Mirror-like glass shine with comforting raspberry and jojoba oils. Never sticky.',
                'description': 'Transform dry lips into luscious, plump pillows with high-wattage shine.',
                'benefits': ['Mirror-glass shine', 'Plumping peptide complex', 'Non-sticky'],
                'how_to_use': 'Wear alone or layer over lipstick.',
                'ingredients': 'Polybutene, Jojoba Seed Oil, Raspberry Seed Oil, Palmitoyl Tripeptide-1.',
                'image': 'https://images.unsplash.com/photo-1625093742435-6fa192b6fb10?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1625093742435-6fa192b6fb10?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Honey Glaze', 'hex': '#EBB692'},
                    {'name': 'Pink Petal', 'hex': '#F0A3AF'}
                ]
            },
            {
                'id': 'gg-tools-07',
                'name': 'The Master Artistry 8-Piece Vegan Brush Set',
                'brand': 'Rose Atelier',
                'category_id': 'brushes-tools',
                'price': 3299.00,
                'original_price': 4299.00,
                'discount': 23,
                'rating': 5.0,
                'reviews_count': 178,
                'is_bestseller': True,
                'is_new_arrival': False,
                'is_featured': True,
                'sku': 'GG-TLS-007',
                'in_stock': True,
                'short_description': 'Ultra-plush synthetic micro-fibers, rose-gold ferrules, and blush wooden handles.',
                'description': '8-piece professional brush wardrobe giving you every tool required for complexion and eyes.',
                'benefits': ['100% cruelty-free bristles', 'Zero shedding', 'Luxury travel clutch'],
                'how_to_use': 'Use for buffing, contouring, and blending.',
                'ingredients': 'Taklon Synthetic Fibers, Birchwood Handle.',
                'image': 'https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Blush & Rose Gold', 'hex': '#DFB0A5'}
                ]
            },
            {
                'id': 'gg-skin-08',
                'name': 'Dew Prep Barrier Moisture Balm',
                'brand': 'Maison de Beauté',
                'category_id': 'skincare',
                'price': 1899.00,
                'original_price': 2299.00,
                'discount': 17,
                'rating': 4.8,
                'reviews_count': 230,
                'is_bestseller': False,
                'is_new_arrival': True,
                'is_featured': True,
                'sku': 'GG-SKN-008',
                'in_stock': True,
                'short_description': 'Ceramide-infused primer moisturizer for a glassy canvas that grips makeup all day.',
                'description': 'The ultimate bridge between skincare and cosmetics. 5 essential ceramides and hyaluronic acid.',
                'benefits': ['Restores moisture barrier', 'Calms redness with Cica', 'Non-comedogenic'],
                'how_to_use': 'Massage onto clean skin 2 minutes before foundation.',
                'ingredients': 'Aqua, Ceramide NP, Centella Asiatica Extract, Sodium Hyaluronate.',
                'image': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80',
                'images': [
                    'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80'
                ],
                'shades': [
                    {'name': 'Universal Translucent', 'hex': '#FAF6F0'}
                ]
            }
        ]

        for p_data in products_data:
            shades_data = p_data.pop('shades', [])
            images_data = p_data.pop('images', [])
            cat_id = p_data.pop('category_id')

            product, created = Product.objects.update_or_create(
                id=p_data['id'],
                defaults={
                    **p_data,
                    'category': cat_objs[cat_id]
                }
            )

            # Shades
            ProductShade.objects.filter(product=product).delete()
            for s in shades_data:
                ProductShade.objects.create(product=product, name=s['name'], hex=s['hex'])

            # Gallery images
            ProductImage.objects.filter(product=product).delete()
            for idx, img_url in enumerate(images_data):
                ProductImage.objects.create(product=product, image_url=img_url, order=idx)

            status_text = "Created" if created else "Updated"
            self.stdout.write(f"  [Product] {status_text} {product.name}")

        # 3. Reviews
        reviews_data = [
            {
                'name': 'Aishwarya Roy',
                'role': 'Verified Buyer, Mumbai',
                'rating': 5,
                'comment': 'The Velvet Petal lipstick is pure luxury! The formula is so weightless and doesn’t settle into fine lines at all.',
                'product_name': 'Velvet Petal Matte Lipstick'
            },
            {
                'name': 'Ananya Sharma',
                'role': 'Beauty Editor, Delhi',
                'rating': 5,
                'comment': 'I swapped my designer foundation for GLOW & GLAM Luminous Silk and I am never looking back. Gives the most ethereal glass skin glow.',
                'product_name': 'Luminous Silk Hydrating Foundation'
            },
            {
                'name': 'Pooja Hegde',
                'role': 'Verified Buyer, Bangalore',
                'rating': 5,
                'comment': 'The Dew Bloom Liquid Blush gives such a fresh, youthful flush. Two tiny dots are enough for both cheeks.',
                'product_name': 'Dew Bloom Liquid Radiant Blush'
            }
        ]

        Review.objects.all().delete()
        for r in reviews_data:
            Review.objects.create(**r)
            self.stdout.write(f"  [Review] Created review by {r['name']}")

        self.stdout.write(self.style.SUCCESS("Successfully seeded all GLOW & GLAM beauty records! ✨"))
