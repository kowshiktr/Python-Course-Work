def ask_question(q_num, question_data):
    print(f"\nQuestion {q_num}: {question_data['question']}")
    for option in ['a', 'b', 'c', 'd']:
        print(f"{option}) {question_data['options'][option]}")
    answer = input("Your answer (a/b/c/d): ").lower()
    
    if answer == question_data['answer']:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is '{question_data['answer']}'")
        return False

def run_quiz(questions):
    print("🧪 Welcome to the Python Quiz Game!")
    score = 0
    for i, q in enumerate(questions, 1):
        if ask_question(i, q):
            score += 1
    print(f"\n🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You're a Python Pro!")
    elif score >= len(questions) * 0.7:
        print("🎉 Great job!")
    elif score >= len(questions) * 0.5:
        print("👍 Good effort! Keep learning.")
    else:
        print("📘 Keep practicing. You'll get better!")

# 20 Python Interview Questions
quiz_questions= [
    {
        'question': "Lambda functions are stored in memory as",
        'options': {
            'a': "Function objects",
            'b': "Methods",
            'c': "Classes",
            'd': "Modules"
        },
        'answer': 'a'
    },
    {
        'question': "What is an anonymous function in Python?",
        'options': {
            'a': "A function without a name",
            'b': "A function without parameters",
            'c': "A function inside a class",
            'd': "A built-in function"
        },
        'answer': 'a'
    },
    {
        'question': "Lambda functions cannot contain",
        'options': {
            'a': "Loops",
            'b': "Return statements",
            'c': "Multiple expressions",
            'd': "All of the above"
        },
        'answer': 'd'
    },
    {
        'question': "The output of list(map(lambda x: x*2, [1,2,3])) is",
        'options': {
            'a': "[2, 4, 6]",
            'b': "[1, 2, 3]",
            'c': "[1, 4, 9]",
            'd': "[2, 3, 4]"
        },
        'answer': 'a'
    },
    {
        'question': "How many expressions can a lambda function contain?",
        'options': {
            'a': "Only one",
            'b': "Multiple",
            'c': "Unlimited",
            'd': "None"
        },
        'answer': 'a'
    },
    {
        'question': "Can a generator yield values from another generator?",
        'options': {
            'a': "No",
            'b': "Yes, but only with a loop",
            'c': "Yes, using yield from",
            'd': "Yes, but only manually"
        },
        'answer': 'c'
    },
    {
        'question': "What does this do? def gen(n): while n > 0: yield n; n -= 1",
        'options': {
            'a': "Counts up from 1 to n",
            'b': "Counts down from n to 1",
            'c': "Loops infinitely",
            'd': "Raises an error"
        },
        'answer': 'c'
    },
    {
        'question': "What is a generator in Python?",
        'options': {
            'a': "A function that returns a list",
            'b': "A function that uses yield to produce values one at a time",
            'c': "A class that generates random numbers",
            'd': "A method that loops infinitely"
        },
        'answer': 'b'
    },
    {
        'question': "Can yield and return coexist in a generator?",
        'options': {
            'a': "No, it’s invalid",
            'b': "Yes, return stops yielding",
            'c': "Yes, return yields a value",
            'd': "No, yield overrides return"
        },
        'answer': 'b'
    },
    {
        'question': "What is the output of this code?\n\ndef gen():\n    yield 1\n    yield 2\n\ng = gen()\nprint(list(g)[0])",
        'options': {
            'a': "1",
            'b': "2",
            'c': "None",
            'd': "Error"
        },
        'answer': 'a'
    },
    {
        'question': "Which of these is NOT a feature of generators?",
        'options': {
            'a': "Lazy evaluation",
            'b': "Memory efficiency",
            'c': "One-time iteration",
            'd': "Storing all values in memory"
        },
        'answer': 'd'
    },
    {
        'question': "Can yield send a value back to the generator with next() alone?",
        'options': {
            'a': "Yes",
            'b': "No, needs send()",
            'c': "Yes, with a loop",
            'd': "No, needs return"
        },
        'answer': 'b'
    },
    {
        'question': "Can a function mimic a generator’s lazy evaluation?",
        'options': {
            'a': "Yes, with a loop",
            'b': "No, it computes fully",
            'c': "Yes, with yield",
            'd': "No, unless recursive"
        },
        'answer': 'c'
    },
    {
        'question': "What is the output of def f(): return 1; print(f())?",
        'options': {
            'a': "1",
            'b': "None",
            'c': "Error",
            'd': "Generator object"
        },
        'answer': 'a'
    },
    {
        'question': "Which of the following will create a list of squared numbers from 1 to 5?",
        'options': {
            'a': "[x**2 for x in range(1, 6)]",
            'b': "[x*2 for x in range(1, 6)]",
            'c': "[x+2 for x in range(1, 6)]",
            'd': "[x//2 for x in range(1, 6)]"
        },
        'answer': 'a'
    },
    {
        'question': 'Which of the following best describes the idea of "list comprehension" in problem-solving?',
        'options': {
            'a': "Breaking down a list into subcategories",
            'b': "Analyzing patterns within a list to generate a new list",
            'c': "Memorizing a list of items without changes",
            'd': "Replacing list elements with random values"
        },
        'answer': 'b'
    },
    {
        'question': "Which of the following statements is true about list comprehension?",
        'options': {
            'a': "It is always slower than loops",
            'b': "It creates a new list without modifying the original",
            'c': "It only works for numeric data",
            'd': "It does not support conditions"
        },
        'answer': 'b'
    },
    {
        'question': "What will be the output of [x + y for x in range(2) for y in range(2)]?",
        'options': {
            'a': "[1, 2, 2, 3]",
            'b': "[0, 1, 2, 3]",
            'c': "[0, 1, 1, 2, 2, 3]",
            'd': "[10, 1, 1, 2]"
        },
        'answer': 'd'
    },
    {
        'question': "Which list comprehension will correctly extract numbers greater than 5 from a list?",
        'options': {
            'a': "[x for x in numbers if x > 5]",
            'b': "[x < 5 for x in numbers]",
            'c': "[5 > x for x in numbers]",
            'd': "[filter(x > 5) for x in numbers]"
        },
        'answer': 'a'
    },
    {
        'question': "What will be the result of [x*3 for x in range(3)]?",
        'options': {
            'a': "[3, 6, 9]",
            'b': "[0, 3, 6]",
            'c': "[1, 3, 6]",
            'd': "[3, 6, 12]"
        },
        'answer': 'b'
    }
]


# Run the game
if __name__== "__main__":
    run_quiz(quiz_questions)
def ask_question(q_num, question_data):
    print(f"\nQuestion {q_num}: {question_data['question']}")
    for option in ['a', 'b', 'c', 'd']:
        print(f"{option}) {question_data['options'][option]}")
    answer = input("Your answer (a/b/c/d): ").lower()
    
    if answer == question_data['answer']:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is '{question_data['answer']}'")
        return False

def run_quiz(questions):
    print("🧪 Welcome to the Python Quiz Game!")
    score = 0
    for i, q in enumerate(questions, 1):
        if ask_question(i, q):
            score += 1
    print(f"\n🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You're a Python Pro!")
    elif score >= len(questions) * 0.7:
        print("🎉 Great job!")
    elif score >= len(questions) * 0.5:
        print("👍 Good effort! Keep learning.")
    else:
        print("📘 Keep practicing. You'll get better!")

# 20 Python Interview Questions
quiz_questions= [
    {
        'question': "Lambda functions are stored in memory as",
        'options': {
            'a': "Function objects",
            'b': "Methods",
            'c': "Classes",
            'd': "Modules"
        },
        'answer': 'a'
    },
    {
        'question': "What is an anonymous function in Python?",
        'options': {
            'a': "A function without a name",
            'b': "A function without parameters",
            'c': "A function inside a class",
            'd': "A built-in function"
        },
        'answer': 'a'
    },
    {
        'question': "Lambda functions cannot contain",
        'options': {
            'a': "Loops",
            'b': "Return statements",
            'c': "Multiple expressions",
            'd': "All of the above"
        },
        'answer': 'd'
    },
    {
        'question': "The output of list(map(lambda x: x*2, [1,2,3])) is",
        'options': {
            'a': "[2, 4, 6]",
            'b': "[1, 2, 3]",
            'c': "[1, 4, 9]",
            'd': "[2, 3, 4]"
        },
        'answer': 'a'
    },
    {
        'question': "How many expressions can a lambda function contain?",
        'options': {
            'a': "Only one",
            'b': "Multiple",
            'c': "Unlimited",
            'd': "None"
        },
        'answer': 'a'
    },
    {
        'question': "Can a generator yield values from another generator?",
        'options': {
            'a': "No",
            'b': "Yes, but only with a loop",
            'c': "Yes, using yield from",
            'd': "Yes, but only manually"
        },
        'answer': 'c'
    },
    {
        'question': "What does this do? def gen(n): while n > 0: yield n; n -= 1",
        'options': {
            'a': "Counts up from 1 to n",
            'b': "Counts down from n to 1",
            'c': "Loops infinitely",
            'd': "Raises an error"
        },
        'answer': 'c'
    },
    {
        'question': "What is a generator in Python?",
        'options': {
            'a': "A function that returns a list",
            'b': "A function that uses yield to produce values one at a time",
            'c': "A class that generates random numbers",
            'd': "A method that loops infinitely"
        },
        'answer': 'b'
    },
    {
        'question': "Can yield and return coexist in a generator?",
        'options': {
            'a': "No, it’s invalid",
            'b': "Yes, return stops yielding",
            'c': "Yes, return yields a value",
            'd': "No, yield overrides return"
        },
        'answer': 'b'
    },
    {
        'question': "What is the output of this code?\n\ndef gen():\n    yield 1\n    yield 2\n\ng = gen()\nprint(list(g)[0])",
        'options': {
            'a': "1",
            'b': "2",
            'c': "None",
            'd': "Error"
        },
        'answer': 'a'
    },
    {
        'question': "Which of these is NOT a feature of generators?",
        'options': {
            'a': "Lazy evaluation",
            'b': "Memory efficiency",
            'c': "One-time iteration",
            'd': "Storing all values in memory"
        },
        'answer': 'd'
    },
    {
        'question': "Can yield send a value back to the generator with next() alone?",
        'options': {
            'a': "Yes",
            'b': "No, needs send()",
            'c': "Yes, with a loop",
            'd': "No, needs return"
        },
        'answer': 'b'
    },
    {
        'question': "Can a function mimic a generator’s lazy evaluation?",
        'options': {
            'a': "Yes, with a loop",
            'b': "No, it computes fully",
            'c': "Yes, with yield",
            'd': "No, unless recursive"
        },
        'answer': 'c'
    },
    {
        'question': "What is the output of def f(): return 1; print(f())?",
        'options': {
            'a': "1",
            'b': "None",
            'c': "Error",
            'd': "Generator object"
        },
        'answer': 'a'
    },
    {
        'question': "Which of the following will create a list of squared numbers from 1 to 5?",
        'options': {
            'a': "[x**2 for x in range(1, 6)]",
            'b': "[x*2 for x in range(1, 6)]",
            'c': "[x+2 for x in range(1, 6)]",
            'd': "[x//2 for x in range(1, 6)]"
        },
        'answer': 'a'
    },
    {
        'question': 'Which of the following best describes the idea of "list comprehension" in problem-solving?',
        'options': {
            'a': "Breaking down a list into subcategories",
            'b': "Analyzing patterns within a list to generate a new list",
            'c': "Memorizing a list of items without changes",
            'd': "Replacing list elements with random values"
        },
        'answer': 'b'
    },
    {
        'question': "Which of the following statements is true about list comprehension?",
        'options': {
            'a': "It is always slower than loops",
            'b': "It creates a new list without modifying the original",
            'c': "It only works for numeric data",
            'd': "It does not support conditions"
        },
        'answer': 'b'
    },
    {
        'question': "What will be the output of [x + y for x in range(2) for y in range(2)]?",
        'options': {
            'a': "[1, 2, 2, 3]",
            'b': "[0, 1, 2, 3]",
            'c': "[0, 1, 1, 2, 2, 3]",
            'd': "[10, 1, 1, 2]"
        },
        'answer': 'd'
    },
    {
        'question': "Which list comprehension will correctly extract numbers greater than 5 from a list?",
        'options': {
            'a': "[x for x in numbers if x > 5]",
            'b': "[x < 5 for x in numbers]",
            'c': "[5 > x for x in numbers]",
            'd': "[filter(x > 5) for x in numbers]"
        },
        'answer': 'a'
    },
    {
        'question': "What will be the result of [x*3 for x in range(3)]?",
        'options': {
            'a': "[3, 6, 9]",
            'b': "[0, 3, 6]",
            'c': "[1, 3, 6]",
            'd': "[3, 6, 12]"
        },
        'answer': 'b'
    }
]


# Run the game
if __name__ == "_main_":
    run_quiz(quiz_questions)
