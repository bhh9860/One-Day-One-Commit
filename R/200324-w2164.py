for num in range(1, 100):
    card = []
    for i in range(num):
        card.append(i+1)
        
    while (len(card) > 1):
        del card[0]
        a = card[0]
        del card[0]
        card.append(a)

    print(num,card)
