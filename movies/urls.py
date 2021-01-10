from django.urls import path
from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView, JsonFilterMovieView, \
    AddStarRating, Search

urlpatterns = [
    path("", MoviesView.as_view()),
    path("filter/", FilterMoviesView.as_view(), name="filter"),
    path("search/", Search.as_view(), name="search"),
    # path("json-filter/", JsonFilterMovieView.as_view(), name="json_filter"),
    path("add-rating/", AddStarRating.as_view(), name="add_rating"),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="actor_detail"),
]
