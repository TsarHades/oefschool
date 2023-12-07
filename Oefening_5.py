# creëer hier de gevraagde functie(s) met implementatie:
def is_gesorteerd(lijst):
    if len(lijst) == 0 or len(lijst) == 1:
        return True
    else:
        for i in range(0 ,len(lijst)-1):
            print(lijst[i])
            print(lijst[i+1])
            if lijst[i] <= lijst[i+1]:
                pass
            else:
                return False
        return True


# testen:
assert is_gesorteerd([])
assert is_gesorteerd([5])
assert is_gesorteerd([3, 7, 11])
assert not is_gesorteerd([3, 7, 5, 11])
assert is_gesorteerd([3, 7, 7, 11])
assert is_gesorteerd(["aaabc", "aab", "b"])
assert not is_gesorteerd(["aabc", "aab", "b"])
