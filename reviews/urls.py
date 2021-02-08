from django.urls import path

from reviews.views import ReviewsListView

urlpatterns = [
    path('', ReviewsListView.as_view(), name='reviews_list'),
]
