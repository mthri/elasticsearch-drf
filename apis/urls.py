from django.urls import path

from apis.views import CarCreateUpdateView, SearchCarView


urlpatterns = [
    path('car/', CarCreateUpdateView.as_view()),
    path('car/search', SearchCarView.as_view()),
]