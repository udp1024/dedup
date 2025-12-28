import os
import hashlib
from collections import defaultdict

def find_size_groups(root):
    size_map = defaultdict(list)
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            try:
                size = os.path.getsize(full)
                size_map[size].append(full)
            except OSError:
                pass
    return {s: f for s, f in size_map.items() if len(f) > 1}

def hash_file(path, block_size=65536):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()

def find_duplicates_by_hash(size_groups):
    hash_map = defaultdict(list)
    for size, files in size_groups.items():
        for f in files:
            try:
                h = hash_file(f)
                hash_map[h].append(f)
            except Exception:
                pass
    return {h: f for h, f in hash_map.items() if len(f) > 1}

def find_duplicates(root):
    size_groups = find_size_groups(root)
    return find_duplicates_by_hash(size_groups)

