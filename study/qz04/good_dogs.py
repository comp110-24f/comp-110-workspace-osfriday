"""Practicing recursive functions for QZ04!"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx + 1 == len(scores)
    if is_good:
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    return is_good
