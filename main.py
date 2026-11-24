#!/usr/bin/env python3
"""Write one funny resignation line to /output/entry.txt. Stdlib only."""
import os

LINE = "I resign effective immediately — my last day was three weeks ago emotionally, and I am taking the office plant, because it chose me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
