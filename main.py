import os
from gensim.summarization.summarizer import summarize


def main():
    file_path = os.environ["INPUT_PATH"]
    summary = "no summary"
    with open(file_path, 'r') as file:
        text = file.read()
    summary = summarize(text)
    print(f"::set-output name=summary::{summary}")


if __name__ == "__main__":
    main()
