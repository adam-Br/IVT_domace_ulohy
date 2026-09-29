import  csv
fr = open("data.csv","r",encoding="utf-8")
reader = csv.reader(fr)

def get_chinese_stats(data):
    needed_data = []
    for line_a in data:
        if line_a[0] == "China":
            needed_data.append(line_a)
    return needed_data

counters = {"0":0,"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0,"9":0}
percent = []
data = get_chinese_stats(reader)
for line in data:
    count = line[5]
    if count.isdigit():
        counters[str(count)[0]] +=1

for i in counters:
    temp = round(counters[i]/len(data)*100,2)
    percent.append(f"{i}: {temp}%")

print(percent)
print(counters)
