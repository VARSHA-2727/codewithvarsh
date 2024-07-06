print("Welcome to KBK")
print("Your 1st question in KBK is:")
# print("Capital of India??")

# questions = [
#         {"question": "What is the capital of India?", "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"], "answer": "B"},
#         {"question": "Who is the author of 'Harry Potter'?", "options": ["A) J.K. Rowling", "B) J.R.R. Tolkien", "C) George R.R. Martin", "D) Stephen King"], "answer": "A"},
#         {"question": "What is the largest planet in our solar system?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "C"},
#         {"question": "Which element has the chemical symbol 'O'?", "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Neon"], "answer": "B"},
#         {"question": "In which year did India gain independence?", "options": ["A) 1942", "B) 1945", "C) 1947", "D) 1950"], "answer": "C"}
#     ]
    
question1 = {
        "question": "What is the capital of India?",
        "options": "A) Mumbai B) New Delhi C) Kolkata D) Chennai",
        "answer": "B"
    }
    
print("\n" + question1["question"])
print(question1["options"])
answer1 = input("Your answer (A/B/C/D): ").strip().upper()
score =0
if answer1 == question1["answer"]:
    print("Correct!")
    score += 1
else:
    print("incorrect please go to school")
