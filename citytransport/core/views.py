from django.shortcuts import render, redirect
from maps.views import get_geocode_city_name, view_map
from .forms import CityForm

# Create your views here.

def home(request):
    """
    This serves as the default home page of the web application
    """
    form = CityForm()
    geocoded_city_name = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            input_city_text = form.cleaned_data['city_name']
            try:
                geocoded_city_name = get_geocode_city_name(input_city_text)
                if geocoded_city_name:  # Ensure that geocoded_city_name is not empty
                    return redirect('view_map', geocoded_city_name=geocoded_city_name)
                else:
                    form.add_error(None, 'Geocoding failed or no results found.')
            except Exception as e:
                print(f"Geocoding error: {e}")
                form.add_error(None, 'Geocoding error occurred.')
    
    return render(request, 'home.html', {'form': form, 'city_data': geocoded_city_name})
