# Week 5 Quality Assignment — Standalone Submission

This folder is a separate assignment and is not connected to the QR project.

## Contents
- `week5/grades.py` and `week5/test_grades.py`: letter-grade kata and tests.
- `week5/legacy_fees.py`: legacy source used for comparison and static analysis.
- `week5/fees.py` and `week5/test_fees.py`: refactored fee calculation and characterization tests.
- `docs/week5/before.txt`: starter report for pre-refactoring tool output.
- `docs/week5/findings.md`: Ruff findings, additional smells, and hidden-bug explanation.
- `docs/week5/after.md`: before/after measurements and pairing reflection.
- `pyproject.toml`: Ruff rules from the lab.
- `.gitignore`: ignores Python virtual-environment/cache files.

## Run locally (from this folder)
```bash
python -m pip install pytest ruff pylint
python -m pytest week5 -v
ruff check week5/legacy_fees.py --statistics
pylint week5/legacy_fees.py
ruff check week5/fees.py
pylint week5/fees.py
```

Copy the actual Ruff and Pylint terminal output into `docs/week5/before.txt`.
Fill the actual after-refactoring measurements and Pylint scores in
`docs/week5/after.md`; do not submit guessed tool scores.

## GitHub submission
Create/open the repository for this assignment only. From the repository root:
```bash
git switch -c week5-quality
git add week5 docs/week5 pyproject.toml .gitignore README.md
git commit -m "Add Week 5 kata and tests"
git commit -am "Refactor tuition fee calculation"
git push -u origin week5-quality
```
Then open a pull request from `week5-quality` into `main`, request your partner's
review, and submit the pull-request URL on the LMS.

The lab asks for pair commits and a `Co-authored-by:` trailer. Make the commits
with your partner and add their real Git author details; do not use placeholder
names or email addresses.
