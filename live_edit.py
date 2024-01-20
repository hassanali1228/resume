import os
import time

if __name__ == "__main__":
    toml_mtime = os.path.getmtime("resume.toml")

    while True:
        if toml_mtime != os.path.getmtime("resume.toml"):
            os.system("python3 generator.py > resume.tex")
            mtime = os.path.getmtime("resume.toml")
            time.sleep(0.2)
