#Storing team points
team1= 119
team2=110
team3= 50
team4= 92
team5=155

total= team1+team2+team3+team4+team5
average= total/5
print("Total team points: ", total)
print("Average team points: ", average)
print()
#Rewards

#Every star is worth 10 points
print("Team 1 gets", team1//10, "stars.")
print("Team 2 gets", team2//10, "stars.")
print("Team 3 gets", team3//10, "stars.")
print("Team 4 gets", team4//10, "stars.")
print("Team 5 gets", team5//10, "stars.")
print()

#Comparing with last week scores
last_week=103
print("Better than last week?  :", average> last_week )
print("Same as last week?  :", average == last_week)
print("At least as good as last week? average :", average >= last_week )
print()

#calculating with bonus points
team1+=30
team2+=30
team3+=30
team4+=30
team5+=30
print("Final Scores")
print("Team 1 = ", team1)
print("Team 2 = ", team2)
print("Team 3 = ", team3)
print("Team 4 = ", team4)
print("Team 5 = ", team5)
