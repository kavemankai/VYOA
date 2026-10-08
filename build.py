#!/usr/bin/env python3
"""Build index.html from story/pages.txt and src/template.html. Runs validate first."""
import subprocess, sys
if subprocess.call([sys.executable, "validate.py"]) != 0:
    sys.exit("Fix validation errors first.")
story = open("story/pages.txt", encoding="utf-8").read().strip()
assert "`" not in story and "${" not in story, "Story text must not contain backticks or ${"
html = open("src/template.html", encoding="utf-8").read().replace("__STORY__", story)
open("index.html", "w", encoding="utf-8").write(html)
print("Wrote index.html")
