def NbCMin(passw):
    count = 0
    for char in passw:
        if char >= 'a' and char <= 'z':
            count += 1
    return count

def NbCMaj(passw):
    count = 0
    for char in passw:
        if char >= 'A' and char <= 'Z':
            count += 1
    return count

def NbCAlpha(passw):
    count = 0
    for char in passw:
        if not (char.isalpha() or char.isdigit()):
            count += 1
    return count

def LongMaj(passw):
    longest = 0
    current = 0
    for char in passw:
        if char >= 'A' and char <= 'Z':
            current += 1
        else:
            if current > longest:
                longest = current
            current = 0
    return max(longest, current) 

def LongMin(passw):
    longest = 0
    current = 0
    for char in passw:
        if char >= 'a' and char <= 'z':
            current += 1
        else:
            if current > longest:
                longest = current
            current = 0
    return max(longest, current)  

def score(passw):
    score = len(passw) * 4
    score += NbCMaj(passw) * 2
    score += NbCMin(passw) * 3
    score += NbCAlpha(passw) * 5
    score -= LongMaj(passw) * 2
    score -= LongMin(passw) * 2
    return score

example_passwword = input("enter a passwword :")
score_of_passwword = score(example_passwword)


if score_of_passwword < 20:
    strength = 'très faible'
elif score_of_passwword <= 40:
    strength = 'faible'
elif score_of_passwword <= 80:
    strength = 'fort'
else:
    strength = 'très fort'

print(strength)