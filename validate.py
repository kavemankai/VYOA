#!/usr/bin/env python3
"""Check story/pages.txt: links, reachability, choice counts, length. Exit 1 on errors."""
import sys
pages, cur = {}, None
for l in open("story/pages.txt", encoding="utf-8"):
    l = l.strip()
    if not l: continue
    if l.startswith("#"): cur = int(l[1:]); pages[cur] = {"t": [], "c": [], "e": False}
    elif l.startswith("> "): pages[cur]["c"].append(int(l.split("=>")[1]))
    elif l == "!END": pages[cur]["e"] = True
    else: pages[cur]["t"].append(l)
errs, warns = [], []
for n, p in pages.items():
    for t in p["c"]:
        if t not in pages: errs.append(f"page {n}: link to missing page {t}")
        if t == n: errs.append(f"page {n}: links to itself")
    if p["e"] and p["c"]: errs.append(f"page {n}: ending has choices")
    if not p["e"] and not 2 <= len(p["c"]) <= 3: errs.append(f"page {n}: needs 2-3 choices, has {len(p['c'])}")
    w = sum(len(x.split()) for x in p["t"])
    if w > 100: warns.append(f"page {n}: {w} words (target 50-100)")
reach, st = {1}, [1]
while st:
    for t in pages.get(st.pop(), {"c": []})["c"]:
        if t in pages and t not in reach: reach.add(t); st.append(t)
for n in sorted(set(pages) - reach): errs.append(f"page {n}: unreachable from page 1")
if 1 not in pages: errs.append("page 1 missing")
for w in warns: print("warn:", w)
for e in errs: print("ERROR:", e)
print(f"{len(pages)} pages, {sum(p['e'] for p in pages.values())} endings, {len(errs)} errors")
sys.exit(1 if errs else 0)
