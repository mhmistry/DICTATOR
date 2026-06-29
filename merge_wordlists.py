# merge_wordlists.py
import os

WORDLISTS_DIR = 'wordlists'
OUTPUT_FILE = 'master_wordlist.txt'  # In root

wordlist_files = [
    'rockyou.txt', 'common_1m.txt', 'darkweb_10k.txt',
    'default_pw.txt', 'names.txt', 'ssh_common.txt', 'xato_10k.txt'
]

all_passwords = set()
print("Merging wordlists from wordlists/ ...")

for fname in wordlist_files:
    path = os.path.join(WORDLISTS_DIR, fname)
    if os.path.exists(path):
        print(f"  Loading {fname}...")
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                pw = line.strip()
                if pw:
                    all_passwords.add(pw)
    else:
        print(f"  Not found: {fname}")

# Write to root
with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    for pw in sorted(all_passwords):
        out.write(pw + '\n')

print(f"\nDone! {len(all_passwords):,} unique passwords → {OUTPUT_FILE}")