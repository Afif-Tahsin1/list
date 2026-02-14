L = [4, 5, 1, 2, 9, 7, 8, 0]
print(f"Original list: {L}")

count = 0

for  i in L:
    count += 1

avg = count/len(L)

print(f"Sum= {count}")
print(f"Avarage: {avg}")

L.sort()

print(f"Smallest element is: {L[0]}")

print(f"Largest elemant is: {L[-1]}")