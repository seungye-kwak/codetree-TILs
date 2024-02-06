a = input()

def others(string):
    s = set(list(a))
    if len(s) >= 2 :
        return 'Yes'
    else :
        return 'No'

print(others(a))