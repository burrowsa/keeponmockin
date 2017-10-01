def staff_members():
    yield "Basil"
    yield "Sybil"
    yield "Polly"
    yield "Manuel"


def calculate_headcount():
    count = 0
    for _ in staff_members():
        count += 1
    return count
