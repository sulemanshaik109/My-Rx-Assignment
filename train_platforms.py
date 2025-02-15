def minPlatforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    n = len(arrivals)
    platforms_needed = 1
    max_platforms = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1

        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms