from .config import BASE_DIR


def reset():
    with open(BASE_DIR / "countdown" / "time.txt", "w+") as f:
        f.write("00:15")


if __name__ == "__main__":
    reset()
