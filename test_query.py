import asyncio
from src.api.advisor import _query_matching_courses

def test():
    import sys
    sys.path.append('.')
    courses = _query_matching_courses(
        target_subject="Data Science",
        countries=["australia"],
        inferred_level="masters",
        student_gpa=7.77
    )
    print("Found courses:", len(courses))

if __name__ == "__main__":
    test()
