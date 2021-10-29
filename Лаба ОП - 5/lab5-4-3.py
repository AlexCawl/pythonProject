def arrival(Hours_departure, Minutes_departure, Hours_road, Minutes_road):
    res_H = (Hours_departure + Hours_road + (Minutes_departure + Minutes_road) // 60)
    res_M = (Minutes_departure + Minutes_road) % 60

    days = Hours_road // 24

    if res_H // 24 > 0:
        days += 1

    res_H %= 24
    print(f"{res_H:02} hours : {res_M:02} minutes")
    print(f"{days} days")


# Hotp = int(input())
# Motp = int(input())
# Hp = int(input())
# Mp = int(input())
arrival(8, 0, 8, 12)
