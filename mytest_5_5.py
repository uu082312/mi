synonyms = [("beautiful", "pretty"),("mom", "mommy"),("quit", "very"),]
def is_synonymous(strings1, strings2):
    s = 0
    for i in synonyms:
        if i[0] in strings1:
            s += 1
        if i[1] in strings2:
            s += 1
        if s == 1:
            return False
    if s > 0 and s % 2 == 0:
        return True
    return False
print(is_synonymous("My mo is very beautiful", "My mommy is quite pretty"))
