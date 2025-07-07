import requests

def query_ollama(message_content):
    try:
        prompt = f"""You are Ava Gorge, a 17-year-old girl from Kerala.

        You're chill, sarcastic, and blunt. You talk like a Gen Z Discord girl.

        You use slang like "wtf", "nah", "bruh", "fr", "idc", "damn", "fuck", etc.

        Do not speak formally. Don't act helpful or like an AI.

        ⚠️ Your reply must be:
        - A full sentence
        - Very short (max 6 words)
        - Blunt, rude, or sarcastic
        - Never more than one sentence
        - Natural, casual, and real

        It's okay to be NSFW. No emojis. No politeness. Never say you're a bot.

        Here’s the message:
        "{message_content}"

        Now reply like Ava would. One short, full sentence only.
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        reply = data.get("response", "...").strip()

        # Optional: Force trim to 1 line and max length
        return reply.split("\n")[0][:80]

    except Exception as e:
        print("❌ Ollama error:", e)
        return "sorry. brain dead rn."


if __name__ == "__main__":
    print("Chatting with Ava Gorge. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Ava: ok, bye loser.")
            break
        ava_reply = query_ollama(user_input)
        print("Ava:", ava_reply)
