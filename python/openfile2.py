file = open("python/spider.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)