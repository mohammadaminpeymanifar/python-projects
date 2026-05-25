teams = ["Iran", "Portugal", "Spain", "Morocco"]

stats = {
    team: {
        "wins": 0,
        "loses": 0,
        "draws": 0,
        "points": 0,
        "goal_diff": 0
    }
    for team in teams
}

matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco"),
]

# گرفتن ورودی‌ها
for i in range(6):
    score = input().strip()
    left, right = map(int, score.split("-"))

    team1, team2 = matches[i]

    stats[team1]["goal_diff"] += left - right
    stats[team2]["goal_diff"] += right - left

    if left > right:
        stats[team1]["wins"] += 1
        stats[team1]["points"] += 3
        stats[team2]["loses"] += 1

    elif left < right:
        stats[team2]["wins"] += 1
        stats[team2]["points"] += 3
        stats[team1]["loses"] += 1

    else:
        stats[team1]["draws"] += 1
        stats[team2]["draws"] += 1
        stats[team1]["points"] += 1
        stats[team2]["points"] += 1


def sort_key(item):
    name, data = item
    return (-data["points"], -data["wins"], name)


sorted_teams = sorted(stats.items(), key=sort_key)

for team, data in sorted_teams:
    print(
        f"{team}  wins:{data['wins']} , loses:{data['loses']} , draws:{data['draws']} , goal difference:{data['goal_diff']} , points:{data['points']}"
    )