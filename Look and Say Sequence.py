#A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:
#Each consecutive value describes the prior value.

num2word = {1: 'one', 2: 'two'}

def Sequence(num):
    i_int=1
    i_str=0
    if num < 10: return ""
    num_list = [int(x) for x in str(num)]
    
    for _ in num_list: 
        say = "{} {}'s".format(num2word[_],num_list[i_int])
        last_duo = ", and {} {}'s".format(num2word[num_list[-2]],num_list[-1]) 

        if num < 100:
            return say
        elif num >= 1000 and num < 10000:            
            say = say[:5] + last_duo[:-2]+"."
            return say
        else:
            i_int+=2
            i_str+=2
            for _ in range(len(num_list)):
                if _ => len(num_list): continue
                say_again = " {} {},".format(num2word[num_list[i_str]],num_list[i_int])
                say = say[:5]+"," + say_again + last_duo[1:]+"."
                i_int+=2
                i_str+=2
                
            return say
        
print(Sequence(1))      #
print(Sequence(11))     # one 1's
print(Sequence(21))     # two 1's
print(Sequence(1211))   # one 2, and one 1.
print(Sequence(111221)) # #one 1, one 2, and two 1's.
print(Sequence(11222112)) # How?? help me