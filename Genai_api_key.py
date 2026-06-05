from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Kyp6Q-JIDNbJPYI05LbiNY-_f6NtkLmur-6UBSccGr4g")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user
    )

    print("Gemini:",response.text)