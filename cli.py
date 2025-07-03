#!/usr/bin/env python3
"""A simple command-line interface to fetch weather information using wttr.in."""

import sys
import requests


def main():
    """Main function to fetch and display weather information."""
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python main.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=10)
    print(response.text)


if __name__ == "__main__":
    main()
