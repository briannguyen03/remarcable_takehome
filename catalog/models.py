from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Actor(models.Model):
    '''
    Actor(actor_name)
    '''
    actor_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.actor_name


class Director(models.Model):
    '''
    Director(director_name)
    '''
    director_name = models.CharField(max_length=200)

    def __str__(self):
        return self.director_name


class Category(models.Model):
    '''
    Category(category_name)
    '''
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    '''
    Tag(tag_name)
    '''
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Movie(models.Model):
    '''
    Movie(movie_title, movie_description, movie_price, movie_release, movie_rating, director, tags, category, actors)
   
    This model assumes that director and movie are one to one, tags and movie are many to many, category to movie are many to one, 
    and actors to movie are many to many

    Ratings are between 1-5. The model validates the input using MinValueValidator, and MaxValueValidator

    '''
    movie_title = models.CharField(max_length=200)
    movie_description = models.TextField()
    movie_price = models.DecimalField(max_digits=6, decimal_places=2)
    movie_release = models.DateField(null=True, blank=True)
    movie_rating = models.IntegerField(default=1, 
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)],
                                       help_text="Rate the movie between 1-5"
                                       )
    
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name="movies")
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.movie_title


