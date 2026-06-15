
print("Checking file health...")

# This counts every single line in the file
count = sum(1 for line in open("rockyou.txt", "r", encoding="latin-1"))

print("Total passwords in file: " + str(count))