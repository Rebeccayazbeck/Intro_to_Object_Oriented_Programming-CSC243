def syntaxCheker(filename):

    file = open(filename,'r')
    line_list =[]
    for line in file:
        line_list.append(line.split(" "))

    count = 0 

    for line in line_list:
        print(line)
        # ":" in conditions
        if "for" in line and not ":" in line:
            count +=1
            print("Syntax error: Missing ':' ")
        if "else" in line and not ":" in line:
            count +=1
            print("Syntax error: Missing ':' ")
        if "if" in line and not ":" in line:
            count +=1
            print("Syntax error: Missing ':' ")
        if "elif" in line and not ":" in line:
            count +=1
            print("Syntax error: Missing ':' ")
        if "while" in line and not ":" in line:
            count +=1
            print("Syntax error: Missing ':' ")

        # identation in conditions:
        if "for" in line and "\n    " not in line and "\t" not in line:
            count +=1
            print("Syntax error: Missing indentation")       
        if "while" in line and "\n    " not in line and "\t" not in line:
            count +=1
            print("Syntax error: Missing indentation")
        if "else" in line and "\n    " not in line and "\t" not in line:
            count +=1
            print("Syntax error: Missing indentation")
        if "if" in line and "\n    " not in line and "\t" not in line:
            count +=1
            print("Syntax error: Missing indentation")
        if "elif" in line and "\n    " not in line and "\t" not in line:
            count +=1
            print("Syntax error: Missing indentation")
 
        # for loops (range, ",", "()")






        if ("for" and "(" and ")" )in line and "range" not in line :
            count += 1
            print ("Syntax error: Missing 'range'")

        if (" if " in line or "elif" in line or "while" in line) and "=" in line  and "==" not in line :
            count +=1
            print("Syntax error: '=' instead of '=='")

        if (" if " in line or "elif" in line or "while" not in line) and ("==" in line and "=" not in line ):
            count +=1
            print("Syntax error: '==' instead of '='")

    print ("you have" ,count, "bugs in your code")

filename = input("Enter file name: ")
syntaxCheker(filename)