from string import ascii_letters, digits
from random import choices
import requests


BASE_URL     = "https://youtube.com/watch?v="
BASE64_CHARS = ascii_letters + digits + "-_"
ERR_PATTERN  = '"status":"ERROR"'


def main(n: int = 1_000) -> None:
    video_ids = ["".join(choices(BASE64_CHARS, k=11)) for _ in range(n)]
    found     = []

    for vid in video_ids:
        video_url = BASE_URL + vid
        response  = requests.get(video_url)

        if ERR_PATTERN in response.text:
            continue

        found.append(video_url)

    print(f"Es wurden {len(found)} Videos gefunden (true)")
    print("-" * 50)
    print("\n".join(found))


if __name__ == "__main__":
    main()
