from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    reviews_count = models.IntegerField(blank=True, null=True)
    book_url = models.URLField()

    # AI fields
    summary = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title