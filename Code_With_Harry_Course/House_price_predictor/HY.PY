import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    lines = text.splitlines()

    data = []

    for line in lines:
        parts = line.strip().split()

        if len(parts) == 3:
            try:
                x = int(parts[0])
                y = int(parts[1])
                char = parts[2]
                data.append((x, y, char))
            except:
                pass

    if not data:
        print("No valid data found.")
        return


    max_x = max(x for x, y, char in data)
    max_y = max(y for x, y, char in data)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]


    for x, y, char in data:
        grid[y][x] = char

    for row in grid:
        print("".join(row))

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5x0_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

decode_secret_message(url)