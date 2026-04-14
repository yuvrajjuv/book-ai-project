from rest_framework.decorators import api_view
from rest_framework.response import Response


# ✅ GET BOOKS
@api_view(['GET'])
def get_books(request):
    books = [
        {"title": "It's Only the Himalayas", "author": "Unknown"},
        {"title": "Libertarianism for Beginners", "author": "Unknown"},
        {"title": "Mesaerion: The Best Science Fiction Stories 1800-1849", "author": "Unknown"},
        {"title": "Olio", "author": "Unknown"},
    ]
    return Response(books)


# ✅ SCRAPER (Dummy)
@api_view(['GET'])
def trigger_scraper(request):
    return Response({"message": "Scraping completed successfully!"})


# ✅ GENERATE AI (FAKE / FREE)
@api_view(['GET'])
def generate_ai_data(request):
    books = [
        {"title": "It's Only the Himalayas"},
        {"title": "Libertarianism for Beginners"},
        {"title": "Mesaerion: The Best Science Fiction Stories 1800-1849"},
        {"title": "Olio"},
    ]

    results = []

    for book in books:
        # 🔥 FAKE AI SUMMARY (FREE)
        summary = f"""
        '{book['title']}' is a fascinating book that explores its core theme in a simple and engaging way.
        This summary is generated to give a quick idea of the book's content and highlights.
        """

        results.append({
            "title": book["title"],
            "author": "Unknown",
            "summary": summary.strip()
        })

    return Response(results)