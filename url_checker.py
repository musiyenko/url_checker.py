#!/usr/bin/env python3

import requests
import sys
from termcolor import cprint
from pathlib import Path
import urllib.parse


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} filename_with_urls")
    sys.exit()

try:
    with open(sys.argv[1], 'r') as f_urls:
        urls = [url.rstrip() for url in f_urls.readlines() if url.strip()]
except IOError:
    cprint("Could not open the file.", 'red')
    sys.exit()

try:
    with open(f'{Path(sys.argv[1]).stem}_result.txt', 'w') as result:
        for url in urls:
            r = requests.get(url)

            if r.status_code == requests.codes.not_found:
                cprint(f'[{r.status_code}] - {urllib.parse.unquote(r.url)}', 'green')
                result.write(urllib.parse.unquote(r.url) + '\n')

except IOError:
    cprint("Could not open the file.", 'red')
    sys.exit()
