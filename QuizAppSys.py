""" QUIZ HAS A TOTAL 3 LEVEL. 
A)LEVEL1 IS GENERAL LEVEL.
B)USER CAN GO ON LEVEL3 IF USER WILL SUCCESSFULLY CLEAR LEVEL 2. MINIMUM SCORE
10 IS REQUIRED TO CLEAR THIS LEVEL.IF SCORE IS LESS THAN 10 THEN EXIT FROM THE SYSTEM.

C)IN LEVEL3 USER CAN GET ONE CHANCE MORE TO RETAKE QUIZ AGAIN WITH NEW QUESTIONS 
IF HIS SOCRE IS LESS THAN 20 USER CAN RETAKE QUIZ -10 FOR INCORRECT RESPONSE 
AND FINALLY GRADE WILL BE SHOWN. """

#*********************************************************************************************
""" LEVEL-1 IMPLEMENTED WITH TUPLE DATA TYPE ANSWERKEY STORED IN SET DATA TYPE(ANS_SET) """
#**********************************************************************************************

from sys import exit
level1_score,level2_score,level3_score=0,0,0

""" TUP_QUES STORE NUMBER OF THE QUESTIONS AND OPTIONS AS WELL AS CORRECT ANS"""

tup_ques=(
    ("Q1)Which of the following cannot be inherited from the base class?\
     \na)Constructor\nb)Function\nc)Destructor","a"),
    ("Q2)Wrapping data and its related functionality into a single entity is known as ?\
     \na)Absstrction\nb)Encapsulation\nc)Polymorphism","b"),
    ("Q3)Which concept allows you to reuse the written code?\
     \na)Encapsulation\nb)Package\nc)Inheritance","c")
    )       

name = input("Enter your name:-").title()
greet = """Hello {name}, Welcome to programming quiz! 
In level 1 you'll be presented with {n} questions.
You got 10 points for each each correct answer.
Good luck and Let's begin!"""
print(greet.format(name=name, n=len(tup_ques)))
print()   

def tup_que_ans():
    """ Check given answer is correct or not.If it is correct level1_score is incremented by 10"""
    global level1_score 
    
    ans_set = set(["b","a","c"]) # CHECKING INVALID INPUT ANSWER,OPTIONS IS STORED INSIDE SET
        
    for index, value in enumerate(tup_ques):
        first_element = value[0]        
        print(first_element)       
        entered_ans = input("Enter the ans (a/b/c):")        
        
        while True:
            try:
                if entered_ans not in ans_set:
                    print("Enter valid input data and select option from (a/b/c).")
                    break
            finally:
                break
        
        if entered_ans != value[1]:
            print("Your answer is incorrect!")
        else:
            print("Answer {} is correct!".format(entered_ans))
            level1_score += 10
    print()
    print("Your total score of Level 1 is {}".format(level1_score))
    print("You have completed LEVEL 1!\n")
    print("----------------------LEVEL 2.------------------------------")
    print("You can go on level 3 if you can successfully clear level2.")
    print("Minimum score 10 is required to clear level2.")
    print("------------------------------------------------------------")
tup_que_ans()

""" LEVEL1 IMPLEMETNATION IS OVER"""
#******************************************************************************
""" LEVEL 2 IMPLEMENT WITH SINGLE INHERITANCE AND LIST DATA TYPE
    PRIVATE/PUBLIC AND STATIC METHOD """    
#******************************************************************************
class Quiz:
    def __init__(self):
        self._qtype1 = "JAVA" # PROTECTED ATTRIBUTE
        self._qtype2 = "C++" 
        
      #def __str__(self):
     #   print("Select the quiz from below options !")
     #   return ("Quiz Type 1:" +str(self._qtype1) +"\n" + "Quiz Type 2:" + str(self._qtype2))
             
    def __repr__(self):
        print("Select the quiz from below options !")
        return 'Quiz Type 1:%s\nQuiz Type 2:%s' %(self._qtype1,self._qtype2)    
        
    def disp_quiz_option(self):
        """ WHICH QUIZ USER WANT TO TAKE """
        
        global choice1
        global choice2
        choice1 = ""
        choice2 = ""
        global level2_score
        
        while True:
            option = input("Enter which quiz (Java/C++) do you want to take?")
            if option.upper() == self._qtype1:
                print("Welcome in Java quiz!")
                choice1 = option.upper()
                break            
            elif option.upper() == self._qtype2:
                print("Welcome in C++ Quiz!")
                choice2 = option.upper()   
                break            
            else:
                print("Invalid choice try again!")
                continue
  
    """ STATIC METHOD NTOHING TO DO WITH CLASS VARIABLE OR OBJECT INSTANCE RELATED DATA
        IN PYTHON TO DEFINE STATIC METHOD @STATICMETHOD DECORATOR USE FOR CLASSMETHOD 
        @CLASSMETHOD USE..FOR INSTANCE METHOD YOU DON'T NEED TO SPECIFY ANY DECORATOR """         
        
    @staticmethod     
    def final_grade():
        """ DISPLAY ALL THREE LEVELS SCORE AS WELL AS GRADE"""
    
        print("*******************************************************")
        print("Total score of the all quiz's are as below!")    
        print("Your total score of Quiz1 is {} out of 30.".format(level1_score))
        print("Your total score of Quiz2 is {} out of 40.".format(level2_score))
        print("Your total score of Quiz3 is {} out of 30.".format(level3_score))
    
        result = level1_score + level2_score + level3_score
        print("Final score of three quizzes are :",result)
    
        if result >=90:
            print("Well done you got A grade.")
        elif result >=80 and result <90:
            print("You got B grade.")
        elif result >=60 and result<80 :
            print("You got C grade.")
        else:
            print("Minimum score 60 is required to pass the quiz.")
        
        print("*******************************************************") 
    
q1=Quiz()
print(q1)
#------------------------------------------------------------------------------
class Derivequiz(Quiz):
    def __init__(self, question, answer):
          self.question = question  # PUBLIC ATTRIB STORE QUE DEFINE INSIDE QUE_LIST
          self.answer = answer # PUBLIC ATTRIB STORE ANSWER FROM ANS_LIST        
          super(Derivequiz,self).__init__() # CALL BASE CLASS CONSTRUCTOR
         
    def sel_quiz_option(self):        
        """ According to selected quiz option respected function
            java_que/__Cpppque() called"""
            
        if choice1 == self._qtype1: # ACCESS PROTECTED ATTRIB FROM BASE CLASS
            self.java_que() # CALL PUBLIC METHOD
            
        elif choice2 == self._qtype2:       
            self.__Cppque()  # CALL PRIVATE METHOD        
            
    def java_que(self):  # PUBLIC METHOD   
        """ FUNCTION ABOUT TO STORE JAVA'S QUE,ANS INSIDE LIST AND CALCULATE SCORE.
        MINIMUM SCORE 10 IS REQUIRED TO CLEAR LEVEL 2"""        
        global level2_score
        
        que_list=[
            "Q1)Which of the following option leads to the portability and security of Java?\
                  \n(a)Bytecode is executed by JVM\n(b)exception handling\n(c)Dynamic binding\n",
                  "Q2)Which of the following is not a Java features?\
                  \n(a)Dynamic\n(b)Object-oriented\n(c)Use of pointers\n",
                  "Q3)What does the expression float a = 35 / 0 return?\
                  \n(a)Not a number\n(b)Infinity\n(c)0\n",
                  "Q4)What is the return type of the hashCode() method in the Object class?\
                  \n(a)int\n(b)object\n(c)void\n"
                  ]
        
        
        print("There are {} questions in this level.\n".format(len(que_list)))
        #print()
        que_list_ans = [
        Derivequiz(que_list[0], "a"),        
        Derivequiz(que_list[1], "c"),
        Derivequiz(que_list[2], "b"),
        Derivequiz(que_list[3], "a")
        ]
        
        ans_set = set(["b","a","c"]) 
        
        i = 0
        while i < len(que_list_ans):
            print(que_list_ans[i].question)
            print("Enter the answer from options (a/b/c).")
            response = input("Enter the answer:") 
            
            """ CHECKING FOR INVALID INPUT DATA """
            while True:
                try:
                    if response not in ans_set:                     
                        print("Enter valid input data and select input data from (a/b/c).")
                        break
                finally:
                    break    
                
            if response == que_list_ans[i].answer:
                level2_score += 10
                print("Your answer is correct!")
                
            else:
                print("Your answer is incorrect!")
                   
            i=i+1
            
        if level2_score >=10:
            print("Your total score of level2 is {}".format(level2_score))
            print("You have successfully clear LEVEL 2.")
            print()             
             
        else:
            print()
            print("Minimum score 10 is required to clear level2.")
            print("Your total score of level2 is {}".format(level2_score))
            print("You can't go on next level3!\n")
            d1.final_grade() # THROUGH DERIVE CLASS OBJECT CALL BASE CLASS METHOD
            exit()   
            
    def __Cppque(self): # YOU CAN DEFINE PUBLIC BUT LEARNING PURPOSE DEFINE PRIVATE METHOD
        """ FUNCTION ABOUT TO STORE JAVA'S QUE,ANS INSIDE LIST AND CALCULATE SCORE.
        MINIMUM SCORE 10 IS REQUIRED TO CLEAR LEVEL 2"""                      
        global level2_score       
        
        que_list=[
            "Q1)Which of the following is not a type of Constructor?\
             \n(a)Friend constructor\n(b)Default constructor\n(c)Parameterized constructor\n",
             "Q2)Out of the following, which is not a member of the class?\
             \n(a)Static function\n(b)Friend function\n(c)Virtual function\n",
             "Q3)How many types of polymorphism are there in C++?\
             \n(a)One\n(b)Three\n(c)Two\n",
             "Q4)Which of the following approach is used by C++?\
             \n(a)Top-down\n(b)Bottom-up\n(c)Both\n"
             ]
        
        print("There are {} C++ questions in this level.\n".format(len(que_list)))
               
        que_list_ans = [
        Derivequiz(que_list[0], "a"),
        Derivequiz(que_list[1], "b"),
        Derivequiz(que_list[2], "c"),
        Derivequiz(que_list[3], "b")
        ]
        
        ans_set = set(["b","a","c"])
        i = 0     
        while i < len(que_list_ans):
            print(que_list_ans[i].question)
            print("Enter the answer from option (a/b/c).")
            response = input("Enter the answer:") 
            
            """ CHECKING FOR INVALID INPUT DATA """
            while True:
                try:
                    if response not in ans_set:
                        print("Enter valid input data and select option from (a/b/c).")
                        break
                finally:
                    break  
            if response == que_list_ans[i].answer:
                level2_score += 10                
                print("Your answer is correct!")
            else:
                print("Your answer is incorrect!")
                       
            i=i+1  
            
        if level2_score >=10:
            print()
            print("Your total score of level2 is {}".format(level2_score))
            print("You have successfully clear LEVEL 2.")           
            
        else:
            print()
            print("Minimum score 10 is required to clear level2.")
            print("Your total score of level2 is {}".format(level2_score))
            print("You can't go on next level3!\n")
            d1.final_grade()
            exit()   
            
    
d1=Derivequiz(0,0)
d1.disp_quiz_option()
d1.sel_quiz_option()

""" LEVEL-2 IMPLEMENTATION IS OVER """
#******************************************************************************

""" LEVEL-3 IMPLEMENTED WITH CLASS (SINGLE INHERITANCE),STATIC METHOD,
    EMPTY LIST AND FILE. CREATE DICT FROM EMPTY LIST USING ZIP() 
    FOR RETAKEQUIZ() DEFINE ANOTHER DICT WITH NORMAL WAY"""
#******************************************************************************

que_list=[]
ans_list=[]

class File_dict(Quiz):# DERIVE ONLY QUIZ CLASS, BCZ FINAL_GRADE() INSIDE IT
    
    def __init__(self):
        """ DEFINE PRIVATE ATTRIBUTE """    
        self.__path1 = "question.txt"
        self.__path2 = "answer.txt"
        
    def chk_exist_file(self): 
        """ There are two file question.txt and answer.txt, from file question is stored
        inside empty list que_list and answer is stored inside ans_list """
        
        try:
            #que_file = open(self.__path1,"r") # VALID BUT LEARNING PURPOSE USE NAME MANGLING
            que_file = open(f1._File_dict__path1) # PRIVATE ATTRIB ACCESS USING NAME MANGLING. 
                                                  # USE NAME MANGLING WHEN USER CREATE OBJECT AND TRY TO ACCESS VALUE OF INSTANCE VAR
            for line in que_file: 
                line1=line.strip()    
                que_list.append(line1)
                
        except FileNotFoundError:
            print("File not found!")
            exit()
        que_file.close()         
        
        try:
            ans_file = open(self.__path2,"r")
            for line in ans_file:
                line2=line.strip()
                ans_list.append(line2)
                
        except FileNotFoundError:
            print("File not found!")
            exit()  
        ans_file.close() 
        
   
    @staticmethod    
    def create_dict_from_file(): 
        """ STORE QUESTION AND ANSWER INSIDE DICT.HERE IF USER'S SCORE IS <20
        THEY GET THE OPTION FOR RETAKE QUIZ WITH NEW QUESTIONS """
        
        global level3_score 
       
        file_dict=dict(zip(que_list,ans_list))
        #print(file_dict)
        """ check for keyerror exception is working
        try:
            print(file_dict["False"])
        except KeyError:
                print("Value can be access by only key! key not found!\n") """
        
        values = file_dict.values()            
        
        print("----------------------LEVEL3 PYTHON QUIZ------------------------------")       
        print("There are {} questions in this level.".format(len(file_dict)))
        print("If your score is less than 20 then you'll get one chance to retake quiz.")
        print("Correct Answer 10 points")
        print("Incorrect Answer -10 points")
        print("------------------------------------------------------------------------")               
        for k,v in file_dict.items():
            print(k)
            answer = input("Enter the answer:")
            
            """ CHECKING FOR INVALID INPUT DATA """
            if answer.upper() not in values:
                print("Enter valid input and select input data from (True/False).")
                
            if answer.upper() == v:
                level3_score = level3_score + 10
                print("Answer is correct and your score is {}".format(level3_score))                                
            else:
                level3_score = level3_score - 10
                print("Your answer is incorrect and your score is {}".format(level3_score))                 
                
        print()        
        print("Your total score of level3 is {}".format(level3_score))
        
#-------------------------------------------------------------------------------------------        
        """ USER GET THE OPTION TO RETAKE QUIZ"""
        if level3_score <20:
            print("----------------------------------------------------------------")
            while True:   
                choice = input("Enter your choice (y/n): Do you want to take quiz again?")
                if choice == 'y' or choice == "Y":
                    print("You get one chance to imporve your score. Good luck!\n")
                    
                    print("Your total score of level3 is:",f1.retake_level3_quiz()) # f1,File_dict.retake_level3_quiz() #STATIC METHOD CALL WITH CLASS NAME
                    print()
                    f1.final_grade()
                    break
                elif choice =="n" or choice=="N":
                    print()
                    f1.final_grade() # FINAl_GRADE() DEFINE INSIDE QUIZ CLASS 
                    break
                else:
                    print("Invalid choice try again!")
                    continue
        else:
            print()
            f1.final_grade() # FINAl_GRADE() DEFINE INSIDE QUIZ CLASS
            
    @staticmethod                       
    def retake_level3_quiz(): 
        """ IF USER'S SCORE<20 AND CHOICE IS YES THEN THIS FUNCTION IS CALLED
            WHEN USER RETAKE QUIZ NEW QUESTIONS SHOULD BE DISPLAY
            CREATE DICTIONARY.KEY ---> QUESTIONS AND VALUE AS A OPTIONS---"""
        
        global level3_score
        level3_score = 0
        
        q1= """Which one of these is floor division?
a./
b.//
c.%"""
        
        q2= """q2) What is the answer to this expression, 22 % 3 is?
a.1
b.7
c.0"""

        q3= """What is the return type of function id?
a.Float
b.Double
c.Int """
        
        questions={q1:"b",q2:"a",q3:"c"}
        values = questions.values()
        #print(values)
        
        for q in questions:
            print(q)
            response=input("Enter the ans (a/b/c):")
            
            """ CHECKING FOR INVALID INPUT DATA """
            if response not in values:
                print("Enter valid input data and select input data from (a/b/c).")
                       
            if response==questions[q]:
                level3_score=level3_score + 10
                print("Answer is correct and your score is {}".format(level3_score))                                
            else:
                level3_score=level3_score - 10
                print("Your answer is incorrect and your score is {}".format(level3_score))                
        
        return level3_score  # it returns it inside while loop retake_level_3_quiz() call
        
f1=File_dict()
f1.chk_exist_file()
f1.create_dict_from_file() 

""" LEVEL3 IMPLEMENTATION IS OVER """
#------------------------------------------------------------------------------
