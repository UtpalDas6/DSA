#balanced or not
def check_balance(exp):
    stack = []
    closing = ['}',']',')']
    opening = ['{','(','[']
    if exp[0] in closing or exp[-1] in opening:
        return("unbalanced")
    for i in exp:
        if i in closing and stack:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return('balanced')
    else:
        return('unbalanced')
print(check_balance("{()}[][{({})]"))