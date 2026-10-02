def main():
    res = input('What time is it? ')
    res = convert(res)

    if res >= 7 and res <= 8:
        print('breakfast time')

    elif res >= 12 and res <= 13:
        print('lunch time')

    elif res >= 18 and res <= 19:
        print('dinner time')

def convert(time:str)->float:
    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours)
    minutes = minutes / 60
    time = hours + minutes
    return time


if __name__ == "__main__":
    main()
# main()
