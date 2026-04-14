import os

def generate_summary_and_genre(title):
    api_key = os.getenv("OPENAI_API_KEY")

    # 🔥 Agar API key nahi hai → dummy data return
    if not api_key:
        return {
            "summary": f"This is a book titled '{title}'. It is an interesting read.",
            "genre": "General"
        }

    # 🔥 Agar API key hai → real AI use karega
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"Give a short summary and genre for the book: {title}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content

        return {
            "summary": text,
            "genre": "AI Generated"
        }

    except Exception as e:
        return {
            "summary": f"Error generating summary for {title}",
            "genre": "Unknown"
        }