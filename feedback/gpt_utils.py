from openai import OpenAI
from django.conf import settings

print("🔐 Loaded OpenAI key:", settings.OPENAI_API_KEY)


# client = OpenAI(api_key= settings.OPENAI_API_KEY)
client = OpenAI(api_key=settings.OPENAI_API_KEY, base_url="https://openrouter.ai/api/v1")


def analyze_feedback(feedback_text):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for product analysis. "
                    "Analyze user feedback and provide the following:\n"
                    "- Sentiment (Positive/Neutral/Negative)\n"
                    "- Key Themes\n"
                    "- Suggestions for improvement\n"
                    "- Needs Attention (Yes/No) — mark Yes if the feedback contains complaints, frustration, confusion, or negative sentiment."},
            {"role": "user", "content": f"Feedback: {feedback_text}"}
        ],
        # temperature=0.7
    )
    return completion.choices[0].message.content


