def readFromFile (filename):
  file = open(filename,'r')
  line_list =[]
  for line in file:
    line_list.append(line.split(" "))
  return line_list

def twopts(line_list):
  count = 0
  for i in range (len(line_list)):
    if "for" in line_list[i] and ":" not in line_list[i] :
      count += 1 
      print("Syntax error: Missing ':' in line", i+1)
    if "else" in line_list[i] and ":" not in line_list[i] :
      count +=1
      print("Syntax error: Missing ':' in line", i+1 )
    if "if" in line_list[i] and ":" not in line_list[i] :
      count +=1
      print("Syntax error: Missing ':' in line", i+1)
    if "elif" in line_list[i] and ":" not in line_list[i] :
      count +=1
      print("Syntax error: Missing ':'  in line", i+1)
    if "while" in line_list[i] and ":" not in line_list[i] :
      count +=1
      print("Syntax error: Missing ':'  in line", i+1)  
  return count 

def indentation(line_list):
  count = 0
  for i in range (len(line_list)):
    if "for" in line_list[i] and (line_list[i+1][0] != ""and line_list[i+1][1] != ""and line_list[i+1][2] != ""and line_list[i+1][3] != ""):
      count +=1
      print("Syntax error: Missing indentation  in line", i+2)       
    if "while" in line_list[i] and (line_list[i+1][0] != ""and line_list[i+1][1] != ""and line_list[i+1][2] != ""and line_list[i+1][3] != ""):
      count +=1
      print("Syntax error: Missing indentation in line", i+2)
    if "else" in line_list[i] and (line_list[i+1][0] != ""and line_list[i+1][1] != ""and line_list[i+1][2] != ""and line_list[i+1][3] != ""):
      count +=1
      print("Syntax error: Missing indentation in line", i+2)
    if "if" in line_list[i] and (line_list[i+1][0] != ""and line_list[i+1][1] != ""and line_list[i+1][2] != ""and line_list[i+1][3] != ""):
      count +=1
      print("Syntax error: Missing indentation in line", i+2)
    if "elif" in line_list[i] and (line_list[i+1][0] != ""and line_list[i+1][1] != ""and line_list[i+1][2] != ""and line_list[i+1][3] != ""):
      count +=1
      print("Syntax error: Missing indentation in line", i+2)
  return count

def equalSign(line_list):
  count = 0
  for i in range (len(line_list)):
    # "=" in condition instead of "=="
    if "for" in line_list[i] and "=" in line_list[i] and "==" not in line_list[i]:
      count += 1 
      print("Syntax error: '=' instead of '==' in condition in line",i+1)
    if "if" in line_list[i] and "=" in line_list[i] and "==" not in line_list[i]:
      count +=1
      print("Syntax error: '=' instead of '==' in condition in line",i+1)
    if "elif" in line_list[i] and "=" in line_list[i] and "==" not in line_list[i]:
      count +=1
      print("Syntax error: '=' instead of '==' in condition in line",i+1)
    if "while" in line_list[i] and "=" in line_list[i] and "==" not in line_list[i]:
      count +=1
      print("Syntax error: '=' instead of '==' in condition in line",i+1)

    # "==" instead of "="  
    if "for" not in line_list[i] and "==" in line_list[i]:
      count += 1 
      print("Syntax error: '==' instead of '=' in line", i+1)
    elif "if" not in line_list[i] and "==" in line_list[i]:
      count +=1
      print("Syntax error: '==' instead of '=' in line", i+1)
    elif "elif" not in line_list[i] and "==" in line_list[i]:
      count +=1
      print("Syntax error: '==' instead of '=' in line", i+1)
    elif "while" not in line_list[i] and "==" in line_list[i]:
      count +=1
      print("Syntax error: '==' instead of '=' in line", i+1)    
  return count       

def operations(line_list):
  count = 0
  signs = ["+","-","*","/","%"]
  for i in range (len(line_list)):
    for j in range (5):
      if len(line_list[i]) >1:
        if line_list[i][1] != "=" and signs[j] in line_list[i]  :
          if "print" in line_list[i]:
            return False
          if "for" in line_list[i]:
            return False
          if "while" in line_list[i]:
            return False
          if "elif" in line_list[i]:
            return False
          if "if" in line_list[i]:
            return False
          else:
            count+=1
            print("Syntax Error : missing '=' in line", i+1)
  return count

def forLoop(line_list):
  count = 0 
  for i in range (len(line_list)):
    if "for" in line_list[i] and "in" in line_list[i]:
      if line_list[i][1] == "in":
        count +=1
        print("Syntax Error: no variable specified in line",i+1)
      if line_list[i][4] == "(":
        if line_list[i][3] != "range":
          count += 1
          print ("Syntax Error: missing 'range' in line", i+1)
        if line_list[i][6] != ")" and "," not in line_list[5:-1]:
          count += 1
          print("Syntax Error:Missing ',' in line", i+1)
  return count 

def condElse(line_list):
  count = 0
  for i in range (len(line_list)):
    if "else" in line_list[i]:
      if ":" in line_list[i]:
        if line_list[i][line_list[i].index(":") + 1]!= "\n":
          count+=1
          print("Syntax Error: 'else' should not include any condition")
      else:
        print ("Syntax Error in 'else' condition")
  return count

def deff(var, line_list, i):
  signs = ["+","-","*","/","%","(",")"]
  if not (var.isdigit() or var in signs or var == "'" or var == '"'):
    count = 0
    for j in range (i-1,-1,-1):
      for var in line_list[j]:
        if deff(var,line_list,j):
          count+=1
    if count == 0 :
        return False
  return True

def defined(line_list):
  count = 0
  for i in range (len(line_list)):
    if "=" in line_list[i] and not deff(line_list[i][line_list[i].index('=') + 1], line_list,i) :
     count +=1
     print("Syntax Error: Charactere not defined in line", i+1)
    
    if "print" in line_list[i]:
      if not deff(line_list[i][line_list[i].index("print") + 2],line_list,i):
        count+=1
        print ("Syntax Error: Charactere not defined in line ", i+1)
  return count

        
def syntaxCheker(filename):

  line_list = readFromFile(filename)
  count = twopts(line_list) + indentation(line_list) + equalSign(line_list) + operations(line_list) + forLoop(line_list) + condElse(line_list) + defined(line_list)

  print ("the lines are counted from 1")
  print ("you have", count, "bugs in your code")

filename = input ("Enter the name of the file correctly: ")
syntaxCheker(filename)