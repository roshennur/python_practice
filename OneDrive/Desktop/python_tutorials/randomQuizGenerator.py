# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# The Quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Lousiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing'}

# Generate 35 quiz files.
for quiz_num in range(22):

    # Create the quiz and answer key files.
    quiz_file = open(f'capitalsquiz{quiz_num+1}.txt', 'w', encoding='UTF-8')
    answer_file = open(f'capitalsquiz_answers{quiz_num+1}.txt', 'w', encoding='UTF-8')

    # Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + f'State Capitals Quiz (Form{quiz_num+1})')
    quiz_file.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for num in range(22):

        # Get right and wrong answers.
        correct_answer = capitals[states[num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # Write the question and answer options to the quiz file.
        quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
        for i in range(4):
            quiz_file.write(f"      {'ABCD'[i]}. { answer_options[i]}\n")
        quiz_file.write('\n')

        # Write the answer key to a file.
        answer_file.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}\n")

    quiz_file.close()
    answer_file.close()






























