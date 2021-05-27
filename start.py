from time import sleep

def main():
    for t in range(10, 0, -1):
        time_str = f'00:{str(t).zfill(2)}'
        print(time_str)
        with open('./time.txt', 'w') as f:
            f.write(time_str)
        sleep(1)
    with open('./time.txt', 'w') as f:
        f.write('Time\'s up!')


if __name__ == '__main__':
    main()
