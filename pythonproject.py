
a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
     if i > 150:
         if i > 500:
             break
         continue
     if i % 5 == 0:
         b.append(i)

print(b)