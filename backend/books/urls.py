from django.urls import path
from .views import get_books, trigger_scraper, generate_ai_data

urlpatterns = [
    path('', get_books),
    path('scrape/', trigger_scraper),
    path('generate-ai/', generate_ai_data),
]