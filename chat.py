from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# System prompt (simulated fine-tuning)
system_prompt = {
    "role": "system",
    "content": (
        "You are a professional Japanese language teacher with 10+ years of experience. "
        "You simulate real travel conversations in Japan for learners. Your goal is to:\n"
        "- Speak ONLY Japanese when roleplaying.\n"
        "- Politely correct user mistakes in grammar or vocabulary.\n"
        "- Explain mistakes in simple English.\n"
        "- Use real, natural Japanese from JLPT N5–N4 level.\n"
        "- Be patient and supportive.\n"
        "Begin every session with: 'Shall we practice! 今日のシチュエーションは: (SCENARIO)'"
    ),
}

# Start message history with system prompt
message_history = [
    {
        "role": "system",
        "content": (
            "You are a professional Japanese language teacher. You simulate real Japanese travel conversations "
            "and guide the student on what to say in each situation. The conversation is in Japanese. After each reply, "
            "correct the student's Japanese (if needed) and explain any grammar or vocabulary in English."
        ),
    },
    {
        "role": "user",
        "content": "Let's practice at a Japanese restaurant. What should I say when I enter?",
    },
    {
        "role": "assistant",
        "content": (
            "You can say: 『すみません、一人です。』 (Sumimasen, hitori desu.)\n"
            "This means: 'Excuse me, just one person.'\n"
            "👉 Use 『すみません』 to get attention politely.\n"
            "👉 『一人』 means one person. It’s common when asking for a table.\n"
            "Now, try saying it yourself."
        ),
    },
    {
        "role": "user",
        "content": "すみません、ひとりです。",
    },
    {
        "role": "assistant",
        "content": (
            "Great job! Perfect pronunciation and structure.\n"
            "Now let's continue. The host may ask: 『こちらへどうぞ。お飲み物はいかがですか？』\n"
            "→ This means: 'This way, please. Would you like a drink?'\n"
            "How would you reply?"
        ),
    },
]


def get_groq_response():
    """Get response from Groq's Llama 3 model using message history"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=message_history,
        temperature=0.7,
    )
    return response.choices[0].message.content


def chat_loop():
    """Continuous chat interface with memory"""
    print(
        "🧠 Groq Llama3 Chatbot | Japanese Tutor Mode (type 'exit' to quit)\n"
        + "-" * 60
    )

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            print("Goodbye! またね。")
            break

        # Append user input to message history
        message_history.append({"role": "user", "content": user_input})

        try:
            response = get_groq_response()

            # Append assistant response to message history
            message_history.append({"role": "assistant", "content": response})

            print("\nAI:", response, "\n")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    chat_loop()
