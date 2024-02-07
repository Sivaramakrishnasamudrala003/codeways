import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Rules:")
        print("1. Answer the questions correctly to score points.")
        print("2. There are multiple-choice and fill-in-the-blank questions.")
        print("3. Have fun!")

    def present_quiz_questions(self):
        for question in self.questions:
            print(question['question'])
            if 'options' in question:
                for i, option in enumerate(question['options'], 1):
                    print(f"{i}. {option}")
            user_answer = input("Your answer: ")
            self.evaluate_user_answer(question, user_answer)
    
    def evaluate_user_answer(self, question, user_answer):
        if 'answer' in question:
            correct_answer = question['answer']
            if user_answer.lower() == correct_answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is: {correct_answer}")
        else:
            print("This is a fill-in-the-blank question. No answer choices provided.")
    
    def display_final_results(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        return choice == 'yes'

# Sample quiz questions
questions = [
    {
        'question': 'What is the capital of Ap?',
        'options': ['amaravathi','vizag','kurnool','none'],
        'answer': 'none'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['William Shakespeare', 'Charles Dickens', 'Jane Austen'],
        'answer': 'William Shakespeare'
    },
    {
        'question': 'what is the easiest way to pass the exam?',
        'options':['Reading','copying','slips'],
        'answer': 'Reading'
    }
]

def main():
    quiz = QuizGame(questions)
    quiz.display_welcome_message()
    
    play = True
    while play:
        quiz.present_quiz_questions()
        quiz.display_final_results()
        play = quiz.play_again()

if __name__ == "__main__":
    main()

