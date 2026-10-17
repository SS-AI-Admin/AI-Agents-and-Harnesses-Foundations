import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from AI agents & Harnesses foundations")
    print(os.environ.get("OPENAI_API_KExY"))


if __name__ == "__main__":
    main()
