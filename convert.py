def to_mins(d, h, m):
    return 1440*d + 60*h + m

def to_dhm(mins):
    d = int(mins/1440)
    mins -= 1440 * d
    h = int(mins/60)
    mins -= 60 * h
    m = mins
    return [d, h, m]