import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the specific DeepSeek key
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("No API Key found! Check your .env for DEEPSEEK_API_KEY.")

# 2. Configure the Client for DeepSeek
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


def translate_blog(japanese_text, author_name):
    """
    Translates Nogizaka46 blogs using DeepSeek V3.
    """
    print(f"   (DeepSeek is translating for {author_name}...)")

    system_instruction = f"""
    You are a professional translator specializing in Japanese Idol blogs (specifically Nogizaka46).
    You are translating a blog post by the member "{author_name}".

    Your Goal:
    Translate the Japanese text into English while preserving the original **voice, emotion, and nuance**.

    Guidelines:
    1. **Tone:** Informal, cute, and conversational. Like a text message to a fan.
    2. **First Person:** Use "I" naturally.
    3. **Slang:** If the text uses (笑), translate it as (lol), (haha), or just haha.
    4. **Formatting:** Keep the paragraph breaks similar to the original.
    5. **Emojis:** Preserve all emojis.
    6. **Accuracy:** Do not summarize. Translate the full content.
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # The specific DeepSeek model name
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": japanese_text}
            ],
            temperature=1.0,  # DeepSeek handles higher temp well for creativity
            stream=False
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error during DeepSeek translation: {e}"


if __name__ == "__main__":
    # Test Run
    print(translate_blog("昨日はありがとう！楽しかったよ (笑)", "DeepSeek Test"))