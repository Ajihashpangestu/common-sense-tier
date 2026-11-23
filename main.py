#!/usr/bin/env python3
"""HR announced the new AI policy is 'just - entry for a make.fun judge bounty."""
import os

LINE = "HR announced the new AI policy is 'just use common sense.' Three people asked if common sense is included in the free tier."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
