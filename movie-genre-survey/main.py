genres = [
    "Horror",
    "Romance",
    "Comedy",
    "History",
    "Adventure",
    "Action"
]

counts = {genre: 0 for genre in genres}

n = int(input())

for _ in range(n):
    data = input().split()
    name = data[0]
    user_genres = data[1:]

    for g in user_genres:
        if g in counts:
            counts[g] += 1

sorted_genres = sorted(
    counts.items(),
    key=lambda x: (-x[1], x[0])
)

for genre, count in sorted_genres:
    print(f"{genre} : {count}")