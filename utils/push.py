from dotenv import load_dotenv
import sys, os

if __name__ == "__main__":
    files = sys.argv
    if len(files) == 1:
        raise ValueError("no files passed in as arguments")#
    files = files[1:]
    print(files)

    load_dotenv()
    email = os.getenv("EMAIL")
    pswd = os.getenv("PSWD")
    print(email, pswd)

    for file in files:
        with open(f"{file}", "r") as f:
            content = f.read()
