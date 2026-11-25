players = []
scores = []
def ReadHighScores():
    file = open("HighScore.txt","r")
    for b in file:
        c = b.strip()
        if c.isdigit():
            scores.append(int(c))
        else:
            players.append(c)
    file.close()

def OutputHighScores():
    for player in range(len(players)):
        print(players[player], "  ", str(scores[player]))


newplayer = input("Enter player name: ")
while len(newplayer) != 3:
    print("Invalid player name")
    newplayer = input("Enter player name: ")
newscore = int(input("Enter score: "))
while newscore<1 or newscore>100000:
    print("Invalid score")
    newscore = int(input("Enter score: "))


def NewHighScores(player, score):
    for i in range(len(scores)):
        if score>scores[i]:
            scores.insert(i,score)
            players.insert(i,player)
            break

def WriteTopTen():
    newfile = open("NewHighScore.txt","w")
    for i in range(0,10):
        newfile.write(players[i]+" "+str(scores[i])+"\n")
    newfile.close()

ReadHighScores()
OutputHighScores()
NewHighScores(newplayer, newscore)
print("\n")
OutputHighScores()
WriteTopTen()

