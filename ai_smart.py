import openai

# Put your API key here
openai.api_key = "YOUR_API_KEY"

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

print(" AI Smart Study Assistant")
print("1. Ask Question")
print("2. Summarize Notes")
print("3. Generate Quiz")

choice = input("Choose option (1/2/3): ")

if choice == "1":
    q = input("Enter your question: ")
    print("\nAnswer:\n", ask_ai(q))

elif choice == "2":
    notes = input("Paste your notes: ")
    prompt = "Summarize this in simple points:\n" + notes
    print("\nSummary:\n", ask_ai(prompt))

elif choice == "3":
    topic = input("Enter topic: ")
    prompt = f"Create 5 MCQ questions on {topic}"
    print("\nQuiz:\n", ask_ai(prompt))

else:
    print("Invalid choice")
