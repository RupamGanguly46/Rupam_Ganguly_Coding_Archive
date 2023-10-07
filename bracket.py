stack = [ ]
openset = [ '(' , '{' , '[' ]
closeset = [ ')' , '}' , ']' ]
ques=input("Enter String")
output='balanced'
for bracket in ques:
    if bracket in openset:
        stack.append(bracket)
    elif bracket in closeset:
        if len(stack)==0:
            output='unbalanced'  
            break
        elif len(stack)>0:
            stackpartner=closeset[openset.index(stack[len(stack)-1])]
            if stackpartner==bracket:
                stack.pop()
            else:
                output='unbalanced'
                break
if len(stack)!=0:
    output='unbalanced'
print(output)


