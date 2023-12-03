for i in range(201):
    result = round((5 * (i ** 3)) / 3 + (45 * (i ** 2)) / 2 + (455 * i) / 6)
    if i < 200:
        next_level_xp = round((5 * ((i + 1) ** 3)) / 3 + (45 * ((i + 1) ** 2)) / 2 + (455 * (i + 1)) / 6)
        xp_required = next_level_xp - result
        print(f"Level {i}: {result} (XP required for next level: {xp_required})")
    else:
        print(f"Level {i}: {result} (Max level)")
