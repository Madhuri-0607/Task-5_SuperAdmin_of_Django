from django.shortcuts import render
from django.db.models import Min, Max
from .models import Product

def product_list(request):
    """
    Beginner-style product list view.
    Shows products with filters for size and price.
    """

    print("👉 Entered product_list view")

    # Step 1: Get all products from database
    try:
        all_products = Product.objects.all()
        print("Total products found:", all_products.count())
    except Exception as e:
        print("❌ Error fetching products:", e)
        all_products = Product.objects.none()

    # Step 2: Get lowest and highest price from database
    min_price = 0
    max_price = 0
    try:
        min_price = all_products.aggregate(Min("price"))["price__min"] or 0
        max_price = all_products.aggregate(Max("price"))["price__max"] or 0
    except Exception as e:
        print("❌ Error getting price range:", e)

    # Step 3: Read filters from request (URL query params)
    selected_size = request.GET.get("size", "")
    min_price_input = request.GET.get("min_price", "")
    max_price_input = request.GET.get("max_price", "")

    print("Filters received: size =", selected_size,
          "min =", min_price_input, "max =", max_price_input)

    # Step 4: Apply filters step by step
    filtered_products = all_products

    # Filter by size
    if selected_size:
        try:
            filtered_products = filtered_products.filter(size=selected_size)
            print("After size filter:", filtered_products.count())
        except Exception as e:
            print("❌ Error filtering by size:", e)

    # Filter by minimum price
    if min_price_input:
        try:
            min_price_value = float(min_price_input)
            filtered_products = filtered_products.filter(price__gte=min_price_value)
            print("After min price filter:", filtered_products.count())
        except Exception as e:
            print("❌ Invalid min price:", e)

    # Filter by maximum price
    if max_price_input:
        try:
            max_price_value = float(max_price_input)
            filtered_products = filtered_products.filter(price__lte=max_price_value)
            print("After max price filter:", filtered_products.count())
        except Exception as e:
            print("❌ Invalid max price:", e)

    # Step 5: Create 5 price ranges (segments) to show in sidebar
    price_segments = []
    try:
        if max_price > min_price:
            gap = (max_price - min_price) / 5
            for i in range(5):
                start = min_price + (gap * i)
                end = min_price + (gap * (i + 1))
                count = Product.objects.filter(price__gte=start, price__lte=end).count()

                price_segments.append({
                    "min": round(start, 2),
                    "max": round(end, 2),
                    "count": count,
                    "label": f"₹{round(start,2)} - ₹{round(end,2)}"
                })
    except Exception as e:
        print("❌ Error creating price segments:", e)

    # Step 6: Count how many products exist for each size
    size_segments = []
    try:
        for code, name in Product.SIZE_CHOICES:
            count = Product.objects.filter(size=code).count()
            size_segments.append({
                "code": code,
                "name": name,
                "count": count
            })
    except Exception as e:
        print("❌ Error counting sizes:", e)

    # Step 7: Send everything to the template
    context = {
        "products": filtered_products.order_by("price"),
        "min_price": round(min_price, 2),
        "max_price": round(max_price, 2),
        "current_min": min_price_input,
        "current_max": max_price_input,
        "selected_size": selected_size,
        "price_segments": price_segments,
        "size_segments": size_segments,
        "available_sizes": Product.SIZE_CHOICES,
    }

    print("👉 Returning", filtered_products.count(), "products to template")
    return render(request, "shop/product_list.html", context)


import csv
from django.http import HttpResponse

def export_products_to_csv(modeladmin, request, queryset):
    """
    Export selected products into a CSV file
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description', 'Price', 'Size'])

    for product in queryset:
        writer.writerow([product.name, product.description, product.price, product.size])

    return response

export_products_to_csv.short_description = "Export Selected Products to CSV"
