#!/usr/bin/env python3
"""Simple prime-checker script.

Usage:
  python3 scripts/prime_checker.py 17

Prints whether the provided integer is prime or not.
"""
import argparse
import sys


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Check if a number is prime")
    parser.add_argument("number", type=int, help="Integer to check")
    args = parser.parse_args()
    n = args.number
    if is_prime(n):
        print(f"{n} is prime")
        return 0
    else:
        print(f"{n} is not prime")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
