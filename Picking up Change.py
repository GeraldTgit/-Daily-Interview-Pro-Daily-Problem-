# Given a string. convert it to dictionary and return the frequency of each character from the string excluding, uppercase letter, whitespace and other special character.
stack=[]
def filter(String):
    for k, val in enumerate(String):
        if String[k].islower() == True and String[k] not in stack:
            stack.append(String[k])
    
    for char in stack:        
        print(f"{char} : {String.count(char)}")
    
Srting = "f
reqUency of LinStr@!"
filter(Srting)
#f : 2
#r : 2
#e : 2
#q : 1
#n : 2
#c : 1
#y : 1
#o : 1
#i : 1
#t : 1
