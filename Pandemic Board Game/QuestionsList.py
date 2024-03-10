import random


class QuestionsList():
    def __init__(self):
        self.questions_list = []


    def GenerateQuestions(self, num_of_player, file_path):
        questions_file = open(file_path, 'r', encoding='cp1252',errors='ignore')
        full_list = []
        text_line = questions_file.readline()
        while text_line != "":
            if text_line == "\n":
                text_line = questions_file.readline()
                continue

            #create a dictionary to store a question and 4 answers and the correct answer, append to full list
            question_set = []
            for i in range(6):
                question_set.append(text_line)
                text_line = questions_file.readline()
            #get rid of some weird text display bug
            question = question_set[0].strip()
            optionA = question_set[1].strip()
            optionB = question_set[2].strip()
            optionC = question_set[3].strip()
            optionD = question_set[4].strip()
            correct_answer = question_set[5].strip().split(":")[1].strip()

            question_dic = {
                    'question': question,
                    'A': optionA,
                    'B': optionB,
                    'C': optionC,
                    'D': optionD,
                    'correct': correct_answer
                }
            
            full_list.append(question_dic)


        #make questions list random
        random.shuffle(full_list)

        #create actual questions list base on players number
        for i in range(num_of_player*3):
            self.questions_list.append(full_list[i])

        return self.questions_list
        
