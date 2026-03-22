from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from .models import Movie, Category, Tag

# Create your views here.


def movie_list(request):
    """
    Movie search and filtering logic. Retreives all movies, categories, and tags, 
    then matches them to the search_querry, or filters applied using the GET request.

    aggregate all of the fields: movies, categories, and tags into a dictionary 'context' for the html to parse
    """
    movies = Movie.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()


    search_querry = request.GET.get('search')
    category_filter = request.GET.get('category')
    tag_filter = request.GET.get('tag')
    rating_filter = request.GET.get('rating')


    if search_querry:
        #Uses django Q objects to search for both the movie title, and description
        #Uses icontains to match tittle and description, case insensitive
        movies = movies.filter(
                Q(movie_title__icontains=search_querry) | Q(movie_description__icontains=search_querry)
                  )

    if rating_filter:
        #Uses gte to get te greater than or equal rating
        movies = movies.filter(movie_rating__gte=rating_filter)

    if category_filter:
        movies = movies.filter(category_id=category_filter)

    if tag_filter:
        #Uses the .distinct() querryset modifier to return distinct entries, and prevent duplicate results
        movies = movies.filter(tags=tag_filter).distinct()


    context = {
            "movies": movies,
            "categories": categories,
            "tags": tags
            }

    return render(request, 'catalog/movies_list.html', context)

   
