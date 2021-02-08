from django.shortcuts import render
from django.views.generic import ListView

from reviews.models import Design


class ReviewsListView(ListView):
    model = Design
    template_name = 'reviews_list.html'
