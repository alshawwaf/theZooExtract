#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

pip install pyzipper

download theZoo from https://github.com/ytisf/theZoo

copy the script tot he extracted zoo folder and run the script

"""

# built-in imports
import sys
import pathlib
import shutil
import zipfile

try:
    import pyzipper
except ImportError as e:
    print('Could not import "pyzipper". Did you install requirements?', file=sys.stderr)
    print(
        'You can always just get "pyzipper" by "pip install --user pyzipper"',
        file=sys.stderr,
    )
    raise e


DECOMPRESSION_PASSWORD = "infected"
OUTPUT_FOLDER = pathlib.Path("malware/OUTPUT")


def extract_files():
    """ """

    INPUT_FOLDER = pathlib.Path("malware/Binaries")
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    # we are using 7z because "zipfile" did not support adding a password
    # Apparently "pyminizip" works just as well.

    # Loop through all files in the directory
        
    for path in INPUT_FOLDER.glob("*"):

        if not path.is_file():
            
            NEW_INPUT_FOLDER = INPUT_FOLDER / path.name

            for zip_file in NEW_INPUT_FOLDER.glob("*"):
                if zip_file.suffix == ".zip":
                    try:
                        with pyzipper.AESZipFile(zip_file) as zf:

                            extracted_files_path = OUTPUT_FOLDER / pathlib.Path(zf.filename).parent
                            zf.extractall(
                                path=extracted_files_path, pwd=bytes(DECOMPRESSION_PASSWORD, "utf-8")
                            )

                            print(f"Info: Extracted ZIP archive to {extracted_files_path}")
                    except Exception as e:
                        print("Extraction Failure:", e)

# if this file is being imported
if __name__ == "__main__":
    extract_files()
