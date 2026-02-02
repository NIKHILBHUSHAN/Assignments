print("enter player name: ")
player_name=input()
no_of_games=int(input("enter of games played: "))
scores=[]
sum=0
print("Enter scores of each games: ")
for i in range(no_of_games):
    score=int(input())
    scores.append(score)
    sum+=score
avg=sum/no_of_games
print(f"Player: {player_name}")
print(f"Games Played: {no_of_games}")
print(f"Total score: {sum}")
print(f"Average Score: {avg}")
