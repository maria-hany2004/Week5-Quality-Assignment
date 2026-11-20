# Week 5 – Static Analysis Findings

## Ruff findings

| Rule | Count | Code smell | Refactoring |
|---|---:|---|---|
| F401 | 2 | Dead code (unused imports) | Delete unused imports |
| PLR2004 | 6 | Magic numbers | Replace values with named constants / an Enum |
| C901 | 1 | High cyclomatic complexity | Replace branching with a rate table |
| PLR0913 | 1 | Too many arguments | Remove unused arguments and group related data |
| ARG001 | 1 | Unused function argument | Remove the unused argument |
| B006 | 1 | Mutable default argument | Use an immutable tuple default |
| E711 / E712 | 1 each | Incorrect None / boolean comparison | Use `is not None` and `if summer` |
| F841 | 1 | Unused local variable | Delete `tmp` |
| N802 | 1 | Invalid function name | Rename `ProcessAll` to `process_all` |

The handout reports 16 Ruff findings in total.

## Additional smells Ruff does not report

1. **Mysterious names:** `d`, `t`, `y`, `s`, and `disc` make the calculation difficult to understand. Use descriptive names such as `courses`, `student_type`, `summer`, and `discount`.
2. **Duplicated logic:** `ProcessAll` repeats almost the same fee-calculation call for student types 1 and 2. A single call using the student's type is clearer.
3. **Mixed responsibilities:** `report` calculates a fee and prints output. Calculation and presentation should be separate; return report text instead.
4. **Primitive obsession:** course data is represented by dictionaries such as `{"h": 3}` instead of a small `Course` data class.

## Hidden bug in ProcessAll

The function has conditions for student types 1 and 2, but no condition for scholarship type 3. Therefore Omar does not receive a newly calculated fee. If Sara is processed first, Omar incorrectly reuses Sara's previous fee (1050); if Omar is first, `fee` has not been assigned and the function raises an error. The refactored `process_all` calculates a fee for every student type.
