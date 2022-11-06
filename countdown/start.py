from time import sleep

from .config import BASE_DIR


def start():
    for t in range(15, 0, -1):
        time_str = f"00:{str(t).zfill(2)}"
        print(time_str)
        with open(BASE_DIR / "countdown" / "time.txt", "w+") as f:
            f.write(time_str)
        sleep(1)
    with open(BASE_DIR / "countdown" / "time.txt", "w+") as f:
        f.write("Time's up!")


if __name__ == "__main__":
    start()
