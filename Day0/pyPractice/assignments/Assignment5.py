def top_three_scores(scores):
    """Return up to three highest scores in descending order."""
    return sorted(scores, reverse=True)[:3]


if __name__ == "__main__":
    print(top_three_scores([75, 92, 88, 95, 80]))  # [95, 92, 88]
