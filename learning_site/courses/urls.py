from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]

@permalink
    def get_absolute_url(self):
        return ('movie_detail', None, {'slug': self.slug})
        
        
# views.py
import render, get_object_or_404
def movie_detail(request, slug, pk):
    movie = get_object_or_404(Movies, slug=slug)

    return render(request, 'movie_detail.html', {'movie' : movie})
    
    
#urls.py
import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', views.movie_detail, name='movie_detail'),

urlpatterns += staticfiles_urlpatterns()

re.sub("[\s]+","_", test)



        
def __str__(self):
        return self.title
        



cd Lytmus/question_3; python manage.py runserver

#movie_detail.html
{% extends "base.html" %}
{% block title %} <h1>{{movie.title}}</h1> {% endblock %}
{% block body%}
<article>
    <header>
    <h1>{{ movie.title }}</h1>
    </header>
</article>
<p data-genre="{{movie.genre}}">Genre: {{ movie.genre }}</p>
<p data-year="{{movie.year}}">Year: {{ movie.year }}</p>
{% endblock %}

#index.html
{% extends "base.html" %}
{% block body %}
<div class="main">
    <h1>Movie Database</h1>
    <h2>Add a Movie <span class="status"></span></h2>
    <form action="{% url 'app.views.add_movie'%}" method="post" class="add-movie">
        <dl>
            <dd>Title:</dd>
            <dt><input id="id-title" type="text" size="30" name="title"></dt>
            <dd>Release Year:</dd>
            <dt><input id="id-year" type="text" size="30" name="year"></dt>
            <dd>Genre:</dd>
            <dt><input id="id-genre" type="text" size="30" name="genre"></dt>
            <dd><input class="add" type="submit" value="Add"></dd>
        </dl>
    </form>
    <h2>All Movies</h2>
    <ol class="movies">
    {% for movie in movies %}
        <li data-id="{{ movie.id }}"><a href="movie/{{movie.slug}}"><span class="title">{{ movie.title }}</span></a> ({{ movie.year }}) - {{ movie.genre}}<a class="delete">X</a></li>
    {% endfor %}
    </ol>
    <div class="noMovies"><em>No movies yet... please, add some below!</em></div>
</div>
{% endblock %}


#base.html
{% load static from staticfiles %}
<!doctype html>
<html>
<head>
    <title>{% block title %} {% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{% static "base.css" %}">
    <script src="{% static "jquery-1.11.1.min.js" %}"></script>
    <script src="{% static "jquery-ui-1.10.4.min.js" %}"></script>
    <script src="{% static "main.js" %}"></script>
</head>
<body>
{% block body %}


{% endblock %}
</body>
</html>

#models.py
"""Models for this Django app"""

from django.db import models
import re

class Movies(models.Model):
    """Model for the movies table in the database"""

    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    year = models.TextField()
    genre = models.TextField()
    slug = models.SlugField(default='', db_index=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = re.sub("[\s]+","_", self.title)
        super(Movies, self).save(*args, **kwargs)

    class Meta:
        """Meta class for Movies model"""

        managed = True
        db_table = 'movies'

#urls.py
"""URL patterns for this Django project"""

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/_add$', views.add_movie, name='add_movie'),
    url(r'^movie/(?P<slug>[-\w.,:\'&]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^api/_delete/(?P<movie_id>\S+)/$', views.delete_movie, name='delete_movie'),
)

urlpatterns += staticfiles_urlpatterns()
