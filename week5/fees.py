"""Refactored tuition-fee calculation."""

from dataclasses import dataclass
from enum import Enum


HOURLY_RATE = 350
STAFF_CHILD_RATE = HOURLY_RATE * 0.5
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


class StudentType(Enum):
    """Supported student fee categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
    """A course represented by its credit/contact hours."""

    hours: int


HOURLY_RATES = {
    StudentType.REGULAR: HOURLY_RATE,
    StudentType.STAFF_CHILD: STAFF_CHILD_RATE,
    StudentType.SCHOLARSHIP: 0,
}


def tuition_fee(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
    extras: tuple[float, ...] = (),
) -> float:
    """Calculate tuition while preserving the legacy fee rules."""
    rate = HOURLY_RATES[student_type]
    total = sum(course.hours * rate for course in courses)
    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE
    total -= discount
    total += sum(extras)
    return total


def fee_report(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
) -> str:
    """Return a human-readable report without printing."""
    amount = tuition_fee(courses, student_type, summer, discount)
    label = {
        StudentType.REGULAR: "Student",
        StudentType.STAFF_CHILD: "Staff child",
        StudentType.SCHOLARSHIP: "Scholarship",
    }[student_type]
    message = f"{label} fee: {amount}"
    if amount > HIGH_FEE_THRESHOLD:
        message += "\nHigh fee"
    return message


def process_all(students: list[dict]) -> dict[str, float]:
    """Calculate a fee for every student, including scholarship students."""
    results = {}
    for student in students:
        student_type = StudentType(student["type"])
        results[student["name"]] = tuition_fee(
            student["courses"],
            student_type,
            student.get("summer", False),
        )
    return results
