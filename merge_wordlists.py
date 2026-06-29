import os

WORDLISTS_DIR = "wordlists"
OUTPUT_FILE = "master_wordlist.txt"

all_passwords = set()

print(f"Merging wordlists from {WORDLISTS_DIR}/ ...")

if not os.path.exists(WORDLISTS_DIR):
    print(f"Error: '{WORDLISTS_DIR}' folder not found.")
    exit()

# Get all .txt files automatically
wordlist_files = [f for f in os.listdir(WORDLISTS_DIR) if f.endswith(".txt")]

if not wordlist_files:
    print("No .txt files found in wordlists folder.")
    exit()

for fname in wordlist_files:
    path = os.path.join(WORDLISTS_DIR, fname)

    print(f"  Loading {fname}...")

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pw = line.strip()
            if pw:
                all_passwords.add(pw)

# Write merged output
print("\nWriting merged wordlist...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for pw in sorted(all_passwords):
        out.write(pw + "\n")

print(f"\nDone! {len(all_passwords):,} unique passwords → {OUTPUT_FILE}")