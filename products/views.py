from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Category
from .forms import ProductForm


def products(request):
    """ This will render the All Products,
    will also render all the search and sorting queries """

    products = Product.objects.all()
    categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    operating_system__icontains=query) | Q(
                        brand__icontains=query) | Q(
                            display__icontains=query) | Q(
                                category__icontains=query)
            products = products.filter(queries)

    products_p = Paginator(products, 1)
    page_number = request.GET.get('page')
    products_page = products_p.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'products_page': products_page,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This will render the selected Product and
    display the information about it """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store inventory 
        Also check if User is Superuser
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorised to access Admin areas!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, 'The new Item has been added to the store inventory')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add the product, please check the form!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product from the store inventory 
        Also check if User is Superuser
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorised to access Admin areas!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'The product has been updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to edit the product, please check the form!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store inventory
        Will render a delete template to check if
        you want to delete the selected product
        Also check if User is Superuser
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorised to access Admin areas!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product has been deleted!')
        return redirect(reverse('products'))

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)