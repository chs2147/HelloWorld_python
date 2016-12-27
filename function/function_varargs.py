def total(initial=5, *numbers, **keywords):
    count = initial

    for number in numbers:
        count += number

    for key in keywords:
        count += keywords[key]
    return count


print total()
print total(1,2,3,4,vege=50,fru=100,bana=40)
