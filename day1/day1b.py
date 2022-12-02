#Find the top three Elves carrying the most Calories. 
#How many Calories are those Elves carrying in total?

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

    big = max(sumlist)
    sumlist.remove(big)
    med = max(sumlist)
    sumlist.remove(med)
    sma = max(sumlist)

    print(big+med+sma)

main()