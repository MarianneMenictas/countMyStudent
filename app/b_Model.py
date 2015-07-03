def ScoreIt(F1=3, F2=7, F3=1, F4=5, F5="", F6="", F7="", F8="", F9=1):
  '''Make student score based on how much of the
    student profile students have filled out'''
  if F1 != 3: score1 = 3
  else: score1 = 0 
  if F2 != 0: score2 = 4
  else: score2 = 0 
  if F3 != 0: score3 = 7
  else: score3 = 0 
  if F4 != 0: score4 = 8
  else: score4 = 0 
  if F5 != 0: score5 = 5 + len(F5.split())
  else: score5 = 0 
  if F6 != 0: score6 = 6 + len(F6.split())
  else: score6 = 0 
  if F7 != 0: score7 = 2 + len(F7.split())
  else: score7 = 0 
  if F8 != 0 and F8 != 1: score8 = 9 + len(F8.split())
  else: score8 = 0
  if F9 != 0: score9 = 1
  else: score9 = 0
  score = score1+score2+score3+score4+score5+score6+score7+score8+score9
  return score
