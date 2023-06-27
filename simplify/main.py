import os
import json
from log import logger

import requests


def main():
    logger.info(f"Hello")

    r = requests.get(
        'https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
    temp = data["forecast"]["temp"]
    logger.info(f"temp in berlin: {temp}")


if __name__ == "__main__":
    main()
