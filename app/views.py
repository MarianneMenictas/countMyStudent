from flask import render_template, request
from app import app
from a_Model import ModelIt
from b_Model import ScoreIt
from c_Model import ActionIt

@app.route('/input')
def cities_input():
  return render_template("input.html")

@app.route('/output')
def cities_output():
  # Select input from input.html file
  dateJoined = int(request.args.get('dateJoinedID',0,type=int))
  gen = int(request.args.get('genderID',0,type=int))
  campusID = int(request.args.get('campusID',0,type=int))
  gradYear = int(request.args.get('gradYearID',0,type=int))
  expDegree = int(request.args.get('expDegreeID',0,type=int))
  gpa = int(request.args.get('gpaID',0,type=int))
  majors = request.args.get('majorsID')
  workExp = request.args.get('workExpID')
  languages = request.args.get('languagesID')
  hobbies = request.args.get('hobbiesID')
  travel = int(request.args.get('travelID',0,type=int))
  socialAct = int(request.args.get('socialActID',0,type=int))
  
  # Feed input values into modules:
  # the_result gives the expected number of applications:
  the_result = ModelIt(dateJoined, gen, campusID, expDegree, gradYear, socialAct, gpa, travel, hobbies, majors, languages, workExp)

  # score_result gives the student score based on how much information was
  # filled out in their profile:
  score_result = ScoreIt(gen, expDegree, gradYear, gpa, hobbies, majors, languages, workExp, travel)

  # action_result gives the recommended action that the student career organisation
  # should carry out to reach out to students.
  action_result = ActionIt(the_result, score_result)

  return render_template("output.html", the_result = the_result, score_result = score_result, action_result = action_result)
