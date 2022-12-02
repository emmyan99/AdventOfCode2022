# Which elf is carrying the most cals?
# Print amount. 

def main():
    input = open("input.txt", "r")
    sum = 0
    sumlist = []
    for line in input:
        if line != "\n":
            sum += int(line)
        else:
            sumlist.append(sum)
            sum = 0
    print(max(sumlist))

main()