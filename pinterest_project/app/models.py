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
