# Week 5 – Before / After

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
|---|---:|---:|
| Ruff issues (total) | 17 | 0 (new/refactored files only) |
| Highest cyclomatic complexity | 9 | 5 or less |
| Arguments of main calculation function | 6 | 5 |
| Pylint score (/10) | 4.86/10 | 10.00/10 |
| Tests passing | 0 | 19 |

## Pairing reflection

We used the driver and navigator approach and discussed each change before implementing it. We wrote tests first so that the refactoring could be checked against the legacy behaviour. Static analysis helped us identify issues such as magic numbers, unused code, and unsafe defaults. We also fixed the scholarship-student bug and verified the new behaviour with tests.