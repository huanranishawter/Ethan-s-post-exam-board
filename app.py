print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 12 + 4?")
  print("   a) 10")
  print("   b) 24")
  print("   c) 16")
  print("   d) 6")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not subtraction."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not multiplication."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not division."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is a biomolecule")
  print("   a) a molecule of life")
  print("   b) biology molecule")
  print("   c) molecule of living things")
  print("   d) molecules that make up living things")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong."
    score -=1
  elif answer == "c":
    output = "Wrong."
    score -=1
    
  elif answer == "d":
    output = "Wrong."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many centimetres make up a metre?")
  print("   a) 1000")
  print("   b) 10")
  print("   c) 1")
  print("   d) 100")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - if 1cm = 0.1m, how many centimetres will make up a metre?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - if 1cm = 0.1m, how many centimetres will make up a metre?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - if 1cm = 0.1m, how many centimetres will make up a metre?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
