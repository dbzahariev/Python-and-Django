ticket = int(input())

count_ticket = 0
for i_1 in range(ord('B'), ord('L') + 1, +2):
    for i_2 in range(ord('f'), ord('a') - 1, -1):
        for i_3 in range(ord('A'), ord('C') + 1):
            for i_4 in range(1, 10 + 1):
                for i_5 in range(10, 1 - 1, -1):
                    count_ticket += 1

                    if count_ticket == ticket:
                        prize = i_1 + i_2 + i_3 + i_4 + i_5
                        print(f"Ticket combination: {chr(i_1)}{chr(i_2)}{chr(i_3)}{i_4}{i_5}\nPrize: {prize} lv.")
