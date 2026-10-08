# Agent instructions

This is a choose-your-own-adventure book: "Lakshmi and Douglass: The Walk That Went Sideways".
Reader age 8. Read-aloud tone: silly, warm, nothing scary for more than a page.

## Where things live
- `story/pages.txt`: the whole book. Edit only this file for story changes.
- `src/template.html`: the web app (styles and logic). Edit for UI changes.
- `index.html`: generated. Never edit by hand. Run `python3 build.py`.
- `validate.py`: checks links and structure. `build.py` runs it automatically.

## Page format (story/pages.txt)
```
#12
Paragraph one.
Paragraph two.
> Choice label => 15
> Another choice => 16
```
An ending page has no choices and the line `!END` instead.

## Rules
- Every non-ending page has 2 or 3 choices. Endings have none.
- Every page must be reachable from page 1. No links to missing pages.
- 50 to 100 words of story text per page.
- Plain text only. No backticks, no `${`, no HTML.
- Every ending must include Douglass getting a treat.
- Recurring characters: Gerald the pigeon (tiny hat, always wrong, wears eleven hats later), Wanda the wheelie bin, Mr Proof the baker, the gnome, Douglass the beagle whose nose leads.
- Part names for the page header are in the `PARTS` list in `src/template.html`. Update it if you add or move zones.
- To insert pages, renumber all links. Keep numbering simple: prefer editing existing pages over inserting.

## Workflow
1. Edit `story/pages.txt`.
2. `python3 build.py` (fails if validation fails).
3. Commit both `story/pages.txt` and the regenerated `index.html`.
