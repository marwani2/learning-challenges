def solve(scores):
   winner = -99999
   runner_up = -99999
   for i in scores:
      if (i > winner):
         winner, runner_up = i, winner
      elif (i < winner and i > runner_up):
         runner_up = i
   return runner_up

scores = [5 , 6 ,54 , 9 , 32 ,32]
print(solve(scores))