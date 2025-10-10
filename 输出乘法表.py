i = 1
j = 1
while i <= 9:
    while j <= i:
        print(f"{i}*{j}={i*j}\t",end="")
        j += 1
    print()
    i += 1
    j = 1;