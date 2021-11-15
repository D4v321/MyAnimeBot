from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd

Subset = pd.read_csv('/Users/davidtigau/Desktop/Interface/cleaned_anime_data.csv', # Change path file for csv in your system
                     nrows=5, usecols=[4, 6, 7, 9, 15])  # Only first 5 rows are shown and the (1,4,6,7, 9,15) columns

Names = []
for i in range(len(Subset["workName"])):
    Names.append(Subset["workName"][i])

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

Highest_Scored_Animes = []

What_Q = []  # Question 1
for item in Names:
    What_Q.append("What is the anime {} about?".format(item))

Review_A = []  # Answer 1
for i in range(len(Names)):
    Review_A.append("Here is a review written by a viwer about the anime {}: {}".format(Names[i], Reviews[i]))

Rating_Q = []  # Question 2
for i in range(len(Names)):
    Rating_Q.append("What rating does the anime {} have?".format(Names[i]))

Score_A = []  # Answer 2
for i in range(len(Names)):
    Score_A.append("The anime {} recieved a score of {} out of 10".format(Names[i], Rating[i]))
    if Rating[i] > 8:
        Highest_Scored_Animes.append(
            "A good anime recomendation would be {} which recived a score of {} out of 10".format(Names[i], Rating[i]))

Author_Q = []  # Question 3
for item in Names:
    Author_Q.append("Who is the author of {} ?".format(item))

Author_A = []  # Answer3
for i in range(len(Names)):
    Author_A.append("{} is the author of {}".format(Author[i], Names[i]))

Episodes_Q = []  # Question 4
for i in range(len(Names)):
    Episodes_Q.append("How many episodes does {} have?".format(Names[i]))

Episodes_A = []  # Answer 4
for i in range(len(Names)):
    Episodes_A.append("{} has a total of {} episodes".format(Names[i], Episodes[i]))

General_Q = []  # Question 5
for i in range(len(Names)):
    General_Q.append("What Animes do you recommend?")
    General_Q.append("What are some good general animes?")

General_A = []  # Answer 5
for item in Highest_Scored_Animes:
    General_A.append(item)

# print(What_Q)
# print(Review_A)
# print(Rating_Q)
# print(Score_A)
# print(Author_A)
# print(Episodes_Q)
# print(Episodes_A)

Anime_Chatbot_List = []


def Question_Answer(Q, A):
    for i in range(len(Names)):
        Anime_Chatbot_List.append(Q[i])
        Anime_Chatbot_List.append(A[i])


def General(Q, A):  # Actually acts more like a specific Q%A (Its size depends on the number of resposnes)
    for i in range(len(A)):
        Anime_Chatbot_List.append(Q[i])
        Anime_Chatbot_List.append(A[i])


Question_Answer(What_Q, Review_A)
Question_Answer(Rating_Q, Score_A)
Question_Answer(Author_Q, Author_A)
Question_Answer(Episodes_Q, Episodes_A)
General(General_Q, General_A)

Anime_Bot = ChatBot('Anime_Champ')

new_trainer = ListTrainer(Anime_Bot)

new_trainer.train(Anime_Chatbot_List)

# CHATBOT PART END