def converting_to_24hr_time(hour, minute, period):
    if 1<=hour<=12 and 0<=minute<=59 and period == "am":
        hour_in_24hr_system = 0

    elif 1<=hour<=12 and 0<=minute<=59 and period=="pm":
        hour_in_24hr_system = hour+12

    else: return "Key in the time correctly so that it can be converted to 24hr clock system"

    return f"{hour_in_24hr_system:02d}{minute:02d} hrs"

print(converting_to_24hr_time(12, 15, "am"))