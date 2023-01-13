from django.urls import include, path
from . import views


urlpatterns = [
   path('create_new_property/', views.home, name="home"),
   path('fetch_property_details/', views.fetch_property_details, name="fetch_property_details"),
   path('update_property_details/', views.update_property_details, name="update_property_details"),
   path('find_cities_by_state/', views.find_cities_by_state, name="find_cities_by_state"),
   path('find_similar_properties/', views.find_similar_properties, name="find_similar_properties"),
]