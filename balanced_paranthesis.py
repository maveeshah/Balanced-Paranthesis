def balanced(expression):
    stack = []
    for i in expression:
        if i == '(':
            stack.insert(0,i)
        elif i == ')' and len(stack) > 0:
            stack.pop(0)
        elif i == ')' and not stack:
            return False
        
    if not stack:
        return True
    else:
        return False

    # if expression.count('(') != expression.count(')'):
    #     return False
    # else:
    #     return True

print(balanced(input()))
