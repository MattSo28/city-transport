from django.shortcuts import render, redirect
from maps.views import get_geocode_city_name, generate_map
from .forms import CityForm

# Create your views here.

def home(request):
    """
    This serves as the default home page of the web application
    """
    form = CityForm()
    geocoded_city_name = None
    
    if request == 'POST':
        if form.is_valid():
            form = CityForm(request.POST)
            input_city_text = form.cleaned_data['city_name']
            try:
                geocoded_city_name = get_geocode_city_name(input_city_text)
                if not geocoded_city_name.empty:
                    return redirect()

            except Exception as e:
                print(f"Geocoding error: {e}")

    return render(request, 'home.html', {'form': form, 'city_data': geocoded_city_name})