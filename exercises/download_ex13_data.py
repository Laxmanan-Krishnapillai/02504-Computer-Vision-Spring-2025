"""Download and extract the data for exercise 13.

Usage
-----
python download_ex13_data.py URL [DEST]

Parameters
----------
URL : str
    Web address of the casper.zip archive.
DEST : str, optional
    Destination directory for the extracted files. Defaults to 'exercises/ex13_data'.
"""

import sys
import urllib.request
import zipfile
import io
from pathlib import Path

def download_and_extract(url: str, dest: str = "exercises/ex13_data") -> None:
    dest_path = Path(dest)
    dest_path.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} ...")
    with urllib.request.urlopen(url) as response:
        data = response.read()
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        zf.extractall(dest_path)
    print(f"Files extracted to {dest_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_ex13_data.py URL [DEST]")
        sys.exit(1)
    url = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) > 2 else "exercises/ex13_data"
    download_and_extract(url, dest)
