def deff(var,line_list,i):
  signs = ["+","-","*","/","%","(",")"]
  if not var.isdigit() or var not in signs and var != "'" or var != '"':
    for j in range (i-1,-1,-1):
      if var not in line_list[j]:
        return False 
  return True  

def defined(line_list):
  count = 0
  for i in range (len(line_list)):
    if "=" in line_list[i] and not deff(line_list[i][line_list[i].index('=') + 1], line_list,i) :

     count +=1
     print("Syntax Error: Charactere not defined in line",i)
    
    if "print" in line_list[i]:
      if not deff(line_list[i][line_list[i].index("print") + 2],line_list,i):
        count+=1
        print ("Syntax Error: Charactere not defined in line ",i+1)
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
