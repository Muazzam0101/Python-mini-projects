# Define the list of questions, answer options, correct answers, and prize amounts
questions = [
    "Which of the following is the largest planet in our solar system?",
    "Who wrote the famous play 'Hamlet'?",
    "Which ocean is the largest by area?",
    "What is the capital city of Canada?",
    "In which year did Christopher Columbus reach the Americas?",
    "Which planet is known as the 'Morning Star' or 'Evening Star'?",
    "Who is the author of the Harry Potter book series?",
    "What is the currency of Japan?",
    "Which famous scientist formulated the laws of motion and universal gravitation?",
    "What is the capital of South Africa?"
]

answers = [
    ["Venus", "Jupiter", "Mars", "Saturn"],
    ["William Wordsworth", "William Shakespeare", "Jane Austen", "Charles Dickens"],
    ["Indian Ocean", "Atlantic Ocean", "Southern Ocean", "Pacific Ocean"],
    ["Toronto", "Ottawa", "Vancouver", "Montreal"],
    ["1492", "1588", "1620", "1776"],
    ["Mars", "Venus", "Mercury", "Jupiter"],
    ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Suzanne Collins"],
    ["Yuan", "Yen", "Won", "Ringgit"],
    ["Galileo Galilei", "Isaac Newton", "Albert Einstein", "Marie Curie"],
    ["Cape Town", "Pretoria", "Johannesburg", "Durban"]
]

prize = ["0","5,000","50,000","100,000","500,000","1000,000","2500,000","5000,000","8000,000","100,00,000","700,00,000"]
correct_answer = ["B","B","D","B","A","B","B","B","B","B"]
count = 0

# Loop through each question
for i in range(len(questions)):
    count += 1
    print("                                     Question no:", count, "\n")
    print(questions[i], "\n\n\n")
    print(" A)", answers[i][0], "\n"
         " B)", answers[i][1], "\n"
         " C)", answers[i][2], "\n"
         " D)", answers[i][3], "\n\n")
    
    # Get user input for the answer
    ans = input("Enter your answer: ")
    
    # Check if the answer is correct
    if ans == correct_answer[i]:
        print("Correct answer!!!\n")
        print("Your total winning prize is", prize[i+1])
        input("Press any key to continue...")
    else:
        # Check if it's the first question or not to determine the total winning prize
        if i == 0:
            print("Wrong answer!\n")
            print("Your total winning prize is", prize[i])
            break
        else:
            print("Wrong answer!\n")
            print("Your total winning prize is", prize[i-1])
            break
    
    # Display the current prize amount
    print("                                     Prize", prize[i], "/-", "\n\n\n")