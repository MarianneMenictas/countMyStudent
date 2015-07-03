def ActionIt(result, score):
  '''Based on student score and predicted number of applications,
     give advice on how this company can reach out to particular
     type of student.'''
  if score == 0 and result == 0:
    ans = "NO. This student is not likely to submit applications in the future."
  if score <=  40:
    ans = "YES. Please e-mail student and encourage them to fill out missing parts of application."
  if score > 40 and result == 0:
    ans = "MAYBE. Student has filled out most parts of application however job listings may not be relevant to student."
  if score > 40 and result == 1:
    ans = "MAYBE. Student has submitted 1 application. It might be worth sending a courtesy e-mail to encourage student to submit more."
  if score > 40 and result > 1:
    ans = "NO. Student has submitted more than 1 application."
  return ans
