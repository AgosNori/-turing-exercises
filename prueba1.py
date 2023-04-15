'''
Given a string s containing just the characters '(','),'{','}',[' and ']', determine if the input string is valid.
An input string is valid if.
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Contraints:
1 <= s.length <= 104
s contains of parentheses only '()[]{}'
'''

#ENTRADAS  #PROCESOS  #SALIDAS


def isValid( s:str)->bool:           
        stack = []
        for c in s:
            
            if c in ['(', '{', '[']:
                stack.append(c)
           
            elif c == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif c == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif c == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
          
            else:
                return False
        return stack == []

if __name__=="__main__":
    line = input()
    if isValid(line):
        print("Valid")
    else:
        print("Invalid")