p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
count = 0
while len(p2) > 0 and len(p1) > 0:
    if count == 10**6:
        print('botva')
        quit(0)
    card1 = p1.pop(0)
    card2 = p2.pop(0)
    if card1 == 0 and card2 == 9:
        p1.append(card1)
        p1.append(card2)
    elif card2 == 0 and card1 == 9:
        p2.append(card1)
        p2.append(card2)
    elif (card1 > card2):
        p1.append(card1)
        p1.append(card2)
    elif (card1 < card2):
        p2.append(card1)
        p2.append(card2)
    #print(count, p1, p2)
    count += 1
if len(p2) == 0:
    print('first', count)
else:
    print('second', count)
