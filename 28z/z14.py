def Unmanned(L: int, N: int, track: list) -> int:
    total = 0
    prev_dist = 0

    for i in range(N):
        dist, red, green = track[i]
        total += dist - prev_dist
        prev_dist = dist

        lights = red + green
        moment = total % lights

        if moment < red:
            total += red - moment

    return total + (L - prev_dist)

