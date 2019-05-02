return_coins = float(input())

count_coin = 0
return_2lv = return_coins // 2
return_coins = round(return_coins - (2 * return_2lv), 2)
return_1lv = return_coins // 1
return_coins = round(return_coins - (1 * return_1lv), 2)
return_50st = return_coins // 0.50
return_coins = round(return_coins - (0.50 * return_50st), 2)
return_20st = return_coins // 0.20
return_coins = round(return_coins - (0.20 * return_20st), 2)
return_10st = return_coins // 0.10
return_coins = round(return_coins - (0.10 * return_10st), 2)
return_5st = return_coins // 0.05
return_coins = round(return_coins - (0.05 * return_5st), 2)
return_2st = return_coins // 0.02
return_coins = round(return_coins - (0.02 * return_2st), 2)
return_1st = return_coins // 0.01
return_coins = return_coins - (0.01 * return_1st)

return_coins_all = return_2lv + return_1lv + return_50st + return_20st + return_10st + return_5st + return_2st
return_coins_all += return_1st

print(f"{return_coins_all:.0f}")
