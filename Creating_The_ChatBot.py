"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response
import pandas as pd

Subset = pd.read_csv ('/content/gdrive/MyDrive/SoftwareEngineering/Data/cleaned_anime_data.csv', nrows = 1000, usecols=[ 4, 6, 7, 9, 15]) #Only first 1000 rows of data are used and the (1,4,6,7, 9,15) columns

#Extracting Names variables from the dataset

Names = []
for i in range(len(Subset["workName"])):
    Names.append(Subset["workName"][i])

clean_names = []

for item in Names:
    cleaned_string = ""
    for letter in item.lower():
        if letter >= 'a' and letter <= 'z':
            cleaned_string += letter  
        else:
            cleaned_string += " "
    clean_names.append(cleaned_string)
        
Names = clean_names

#Extracting the other variables from the dataset
    
Reviews = []
for i in range(len(Subset["Review"])):
    Reviews.append(Subset["Review"][i])

Rating = []
for i in range(len(Subset["overallRating"])):
    Rating.append(Subset["overallRating"][i])
    
Author = []
for i in range(len(Subset["author"])):
    Author.append(Subset["author"][i])
    
Episodes = []
for i in range(len(Subset["episodesSeen"])):
    Episodes.append(Subset["episodesSeen"][i])



Anime_Chatbot_List = [] #The list that will be used to train the chatbot

#The Functions for combining the questions and answers into one list for training


def Question_Answer(Q,A):
  #Input is two lists, one which represents the Question for Q and the other one represents the Answers for A
  #Both of these lists need to be the same size
  #The first item in the list (index 0)  is taken from list Q and appended into the Anime_Chatbot_List and then the same is done for the first item in list A
  #After every cycle of the loop the index is increased by 1
  #This is repeated,until all items in both lists have been added to the Anime_Chatbot_List
    for i in range(len(Names)):
        Anime_Chatbot_List.append(Q[i])
        Anime_Chatbot_List.append(A[i])
        #print(Q[i])
        #print(A[i])
        #print()

        
def Specific(Q,A): 
  #This is a variation of the function above, where the lists do not have to be the same size
  #This is for instances where the Answer list is shorter than the Question list
  #For Example: When the answer list only contains aninmes that have a rating higher than 8 and we do not know how many there will be
  #This Behaves like the Question_Answer function but it stops once all the items in the Answer list have beened appended to the Anime_Chatbot_List
    for i in range(len(A)):
        Anime_Chatbot_List.append(Q[i])
        Anime_Chatbot_List.append(A[i])
        #print(Q[i])        
        #print(A[i])
        #print()


    
#Making the questions and the answers for the chatbot (And using the function to merge them all together into Anime_Chat_Bot_List)
  

Review_Q = [] #Question 1
for item in Names:
    Review_Q.append("what is the anime {} about?".format(item))
    
Review_A = [] #Answer 1
for i in range(len(Names)):
    Review_A.append("here is a review written by a viwer about the anime {}: {}".format(Names[i],Reviews[i]))

Question_Answer(Review_Q, Review_A)



Highest_Scored_Animes = [] #This is defined here to gather the input from the rating, but will be used in a different question and answer pair

        
Rating_Q = [] #Question 2
for i in range(len(Names)):
    Rating_Q.append("what rating does the anime {} have?".format(Names[i]))
    
Rating_A = [] #Answer 2
for i in range(len(Names)):
    Rating_A.append("the anime {} recieved a score of {} out of 10".format(Names[i], Rating[i]))
    if Rating[i] > 8:
        Highest_Scored_Animes.append("a good anime recomendation would be {} which recived a score of {} out of 10".format(Names[i],Rating[i]))

Question_Answer(Rating_Q, Rating_A)
    
    
Author_Q = [] #Question 3
for item in Names:
    Author_Q.append("who is the author of {} ?".format(item))

Author_A = [] #Answer3
for i in range(len(Names)):
    Author_A.append("{} is the author of {}".format(Author[i], Names[i]))

Question_Answer(Author_Q, Author_A)
        

Episodes_Q = [] #Question 4
for i in range(len(Names)):
    Episodes_Q.append("how many episodes does {} have?".format(Names[i]))
    
Episodes_A = [] #Answer 4
for i in range(len(Names)):
    Episodes_A.append("{} has a total of {} episodes".format(Names[i], Episodes[i]))


Question_Answer(Episodes_Q, Episodes_A)

    
    
Recommend_Q = [] #Question 5
for i in range(len(Names)):
    Recommend_Q.append("what animes do you recommend?")
    Recommend_Q.append("what are some good general animes?")

Recommend_A = [] #Answer 5
for item in Highest_Scored_Animes:
    Recommend_A.append(item)


Specific(Recommend_Q, Recommend_A)
    

Favorite_Q = [] #Question 6
Favorite_Q.append("what's your favorite anime?")

Favorite_A = [] #Answer 6
Favorite_A.append("my favorite anime is cowboy bepop")
    

Specific(Favorite_Q, Favorite_A)


#We will now be creating the chatbot and training it

Anime_Bot = ChatBot('Anime_Wizard', read_only=True)

new_trainer = ListTrainer(Anime_Bot)
new_trainer.train(Anime_Chatbot_List)





"""
#Now we will be checking the chatbot

#Checking Question 1

for i in range(5):
  answer = Anime_Bot.get_response(Review_Q[i])
  print(Review_Q[i])
  print(answer)
  print()

#Checking Question 2
for i in range(5):
  answer = Anime_Bot.get_response(Rating_Q[i])
  print(Rating_Q[i])
  print(answer)
  print()

#Checking Question 3
for i in range(5):
  answer = Anime_Bot.get_response(Author_Q[i])
  print(Author_Q[i])
  print(answer)
  print()

#Checking Question 4
for i in range(5):
  answer = Anime_Bot.get_response(Episodes_Q[i])
  print(Episodes_Q[i])
  print(answer)
  print()


#Checking Question 5
for i in range(len(Recommend_A)):
  answer = Anime_Bot.get_response(Recommend_Q[i])
  print(Recommend_Q[i])
  print(answer)
  print()
  

#Checking Question 6
for i in range(len(Favorite_A)):
  answer = Anime_Bot.get_response(Favorite_Q[i])
  print(Favorite_Q[i])
  print(answer)
  print()


#Ask Any question
while True:
  new_question = input("User Question: ")
  answer = Anime_Bot.get_response(new_question)
  print(answer)
  if new_question == "":
    break

"""

"""
