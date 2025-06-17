# Requirements:
# pip install groq  # Install the official Groq Python SDK
# Python 3.7+       # Ensure you're using Python version 3.7 or higher

from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")


def get_groq_response(user_input):
    """Get response from Groq's Llama 3 model"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7,  # Controls randomness (0.0 to 1.0)
    )
    return response.choices[0].message.content


def chat_loop():
    """Continuous chat interface"""
    print("Groq Chatbot with Llama 3 8B (Type 'exit' to quit)\n" + "-" * 50)

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        try:
            response = get_groq_response(user_input)
            print("\nAI:", response, "\n")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    chat_loop()
