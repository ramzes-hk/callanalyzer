numbers = []
with open("C:/Users/ramze/Downloads/never-contacted-2025-12-24 (2).csv") as f:
    for line in f:
        numbers.append(line.split(",")[3].replace("-", ""))


called = []
with open("C:/Users/ramze/Downloads/RecordingsDetailsReport_20251206_122853_AAB.csv") as f:
    for line in f: 
        called.append(line.split(",")[6].replace("+1", ""))

d = 0
for n in numbers:
    if n in called:
        d += 1
        print(n)
print(d)
    
