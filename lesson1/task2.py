while True:
    seconds = int(input('Введите время в секундах: '))
    if seconds > 0:
        h = seconds // (60 * 60)
        seconds = seconds - h * 60 * 60
        i = seconds // 60
        seconds = seconds - i * 60
        if h < 10:
            h = '0' + str(h)
        if i < 10:
            i = '0' + str(i)
        if seconds < 10:
            seconds = '0' + str(seconds)
        print(f'{h}:{i}:{seconds}')
        break