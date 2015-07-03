def ModelIt(F1=1, F2=3, F3=0, F4=7, F5=1, F6=1, F7=5, F8=0, F9="", F10="", F11="", F12=""):

  # Import relevant modules:
  import pandas as pd
  from sklearn.externals import joblib

  # Feed in pickle file from Multi-class Random Forest model fit:
  # User must specify directory here:
  randForrestClf = joblib.load('directory/app/randForrestClf/randForrestClf.pkl')
  
  # Standardise input. Mean and standard deviation values taken from
  # original features.
  # For privacy purposes the mean and standard deviation cannot be specified.
  # User can specify these values based on data.
  F1norm = (F1 - F1mean)/F1stdev ; F2norm = (F2 - F2mean)/F2stdev         
  F3norm = (F3 - F3mean)/F3stdev ; F4norm = (F4 - F4mean)/F4stdev      
  F5norm = (F5 - F5mean)/F5stdev ; F6norm = (F6 - F6mean)/F6stdev      
  F7norm = (F7 - F7mean)/F7stdev ; F8norm = (F8 - F8mean)/F8stdev

  # F9 - F12 are text responses. Count number or words in response:
  F9 = len(F9.split())
  if F9 == 1 or F9 == 2: F9 = 1
  if F9 == 3 or F9 == 4: F9 = 2
  if F9 >= 5 and F9 <=10: F9 = 3
  if F9 >= 10: F9 = 4
  F9norm = (F9 - F9mean)/F9stdev
  
  F10 = len(F10.split())
  if F10 >= 7: F10 = 7
  F10norm = (F10 - F10mean)/F10stdev
  
  F11 = len(F11.split())
  if F11 >= 4: F11 = 4
  F11norm = (F11 - F11mean)/F11stdev
  
  F12norm = len(F12.split())
  if F12 >= 9: F12 = 9
  F12norm = (F12 - F12mean)/F12stdev  
  
  # Bring in coefficients based on standardised data:
  ans = pd.DataFrame([F1norm, F2norm, F3norm, F4norm, F5norm, F6norm,
                      F7norm, F8norm, F9norm, F10norm, F11norm, F12norm])
  predVal = randForrestClf.predict(ans.T)[0]

  # Return the predicted number of applications for specific type of student:
  return predVal
