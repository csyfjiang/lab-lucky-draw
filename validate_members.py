#!/usr/bin/env python3
"""
Lab Members Validator
Sorts member list and checks for duplicates.
"""

import sys
from pathlib import Path


def load_members(csv_file: str) -> list[str]:
    """Load members from CSV file (one name per line)."""
    members = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        for line in f:
            name = line.strip()
            if name:
                members.append(name)
    return members


def find_duplicates(members: list[str]) -> list[str]:
    """Find duplicate names in the list."""
    seen = set()
    duplicates = []
    for member in members:
        if member in seen and member not in duplicates:
            duplicates.append(member)
        seen.add(member)
    return duplicates


def save_members(members: list[str], csv_file: str):
    """Save sorted members to CSV file (one name per line)."""
    with open(csv_file, 'w', encoding='utf-8') as f:
        for member in members:
            f.write(f"{member}\n")


def main():
    csv_file = Path(__file__).parent / "lab_members.csv"

    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        sys.exit(1)

    # Load members
    print(f"Loading members from {csv_file.name}...")
    members = load_members(csv_file)
    print(f"Total members: {len(members)}\n")

    # Check for duplicates
    duplicates = find_duplicates(members)
    if duplicates:
        print("Found duplicates:")
        for dup in duplicates:
            print(f"  - {dup}")
        print()

    # Sort and remove duplicates
    sorted_members = sorted(set(members))
    print(f"Unique members after sorting: {len(sorted_members)}\n")

    # Show preview
    print("First 10 members:")
    for member in sorted_members[:10]:
        print(f"  {member}")

    if len(sorted_members) > 10:
        print("  ...")
        print(f"\nLast 5 members:")
        for member in sorted_members[-5:]:
            print(f"  {member}")

    # Ask for confirmation
    print(f"\n{'='*50}")
    response = input(f"Save sorted list to {csv_file.name}? (y/n): ").strip().lower()

    if response == 'y':
        # Save sorted members (overwrite original)
        save_members(sorted_members, csv_file)
        print(f"Saved {len(sorted_members)} members to {csv_file.name}")
        print("Done!")
    else:
        print("Cancelled. No changes made.")


if __name__ == "__main__":
    main()
