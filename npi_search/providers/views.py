from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Provider
from .forms import ProviderSearchForm

def search_page(request):
    """search page view"""
    form = ProviderSearchForm()
    results = None
    query_performed = False
    
    if request.method == 'GET' and any(request.GET.values()):
        form = ProviderSearchForm(request.GET)
        query_performed = True
        
        if form.is_valid():
            results = search_providers(form.cleaned_data)
            # paginate results
            paginator = Paginator(results, 25)  #  25 results per page
            page_number = request.GET.get('page')
            results = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'results': results,
        'query_performed': query_performed,
    }
    
    return render(request, 'providers/search.html', context)

def search_providers(search_data):
    """search logic for providers based on search criteria"""
    queryset = Provider.objects.all()
    
    # name search (first name and last name)
    if search_data.get('first_name'):
        queryset = queryset.filter(
            first_name__icontains=search_data['first_name']
        )
    
    if search_data.get('last_name'):
        queryset = queryset.filter(
            last_name__icontains=search_data['last_name']
        )
    
    # city search (partial match)
    if search_data.get('city'):
        queryset = queryset.filter(
            city__icontains=search_data['city']
        )
    
    # state search (exact match)
    if search_data.get('state'):
        queryset = queryset.filter(state=search_data['state'])
    
    # postal code search (partial match)
    if search_data.get('postal_code'):
        queryset = queryset.filter(
            postal_code__icontains=search_data['postal_code']
        )

    # taxonomy search (partial match)
    if search_data.get('taxonomy'):
        queryset = queryset.filter(
            primary_taxonomy__icontains=search_data['taxonomy']
        )
    
    return queryset.select_related().order_by('last_name', 'first_name')

def provider_detail(request, npi):
    """Provider detail view by NPI number."""
    provider = get_object_or_404(Provider, npi=npi)
    
    context = {
        'provider': provider,
    }
    
    return render(request, 'providers/detail.html', context)