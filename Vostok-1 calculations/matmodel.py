import math
import json

import graphics_final

def p(h):
    dict = {
    0: 1.225,
    2500: 0.898,
    5000: 0.642,
    7500: 0.446,
    10_000: 0.288,
    15_000: 0.108,
    20_000: 0.040,
    25_000: 0.015,
    30_000: 0.006,
    40_000: 0.001,
    50_000: 0,
    60_000: 0,
    70_000: 0
    }
    keys = list(dict.keys())
    for i in range(len(keys) - 1):
        if keys[i] <= h and h <= keys[i + 1]:
            if abs(keys[i] - h) <= abs(keys[i + 1] - h):
                return dict[keys[i]]
            else:
                return dict[keys[i + 1]]
    return dict[70_000]


def angle(h):
    global turn_angle
    alpha = 90 - turn_angle
    frac = ((h * 0.8 - 600) / (38_000 - 600))
    new_turn_angle = frac * 90
    if abs(new_turn_angle - turn_angle) > 0.4:
        turn_angle = new_turn_angle
        alpha = 90 - turn_angle
    return alpha


def Cd(alpha):
    if alpha >= 45 and alpha <= 135:
        return 3
    elif alpha <= 45 and alpha >= -45 or alpha >= 135 and alpha <= 225:
        return 10


h = 87
t = 0
v = 0
turn_angle = 0
Ft = 839_000
u = 3.53171718 * 10 ** 6
R = 600 + h
m0 = 37_743
P = Ft
I = 250
m_v = P / I
m = m0 - m_v * t
Fg = 9.81 * 600 ** 2 / R ** 2#u * m / R ** 2
A = 1.76
Fd = 0.5 * p(h) * (v ** 2) * Cd(angle(h)) * A
h_l = []
v_l = []
t_l = []
a = 0
h_l.append(int(h))
v_l.append(int(v))
t_l.append(t * 10)



while h <= 38_000:
    t += 0.33
    a = (Ft * math.cos((90 - angle(h)) / 360 * math.pi * 2) - Fd - Fg) / m
    v = v + a * t
    h = h + v * t
    R = 600 + h
    Fg = 9.81 * 600 ** 2 / R ** 2#u * m / R ** 2
    Fd = 0.5 * p(h) * (v ** 2) * Cd(angle(h)) * A
    m = m0 - m_v * t
    h_l.append(int(h))
    v_l.append(int(v))
    t_l.append(t * 10)
    print(int(h), int(m), int(v))
print("--------------------------")
m = m - 8_000
Ft = 215_000 * 0.5
I = 320
P = Ft
m_v = P / I
m0 = m
R = 600 + h
print(m)

while m >= 7_300 and False:
    print(int(h), int(m), int(v), a)
    t += 0.3
    a = (Ft * math.cos((90 - 8) / 360 * math.pi * 2) - Fd - Fg) / m
    v = v + a * t
    h = h + v * t
    R = 600 + h
    Fg = 9.81 * 600 ** 2 / R ** 2#u * m / R ** 2
    Fd = 0.5 * p(h) * (v ** 2) * Cd(8) * A
    m = m0 - m_v * t
    h_l.append(int(h))
    v_l.append(int(v))
    t_l.append(t * 10)

print(int(h))
m = m - 3500
Ft = 0
I = 345
P = Ft
m_v = P / I
m0 = m
R = 600 + h
print("--------------------------")
while h <= 167_000 and False:
    print(int(h), int(m), int(v), a)
    t += 0.3
    a = (Ft * math.cos((90 - 0) / 360 * math.pi * 2) - Fd - Fg) / m
    v = v + a * t
    h = h + v * t
    R = 600 + h
    Fg = 9.81 * 600 ** 2 / R ** 2#u * m / R ** 2
    Fd = 0.5 * p(h) * (v ** 2) * Cd(0) * A
    m = m0 - m_v * t
    h_l.append(int(h))
    v_l.append(int(v))
    t_l.append(t * 10)



s = [h_l, v_l, t_l]
with open("data_mat_model.json", "w") as file_data:
    json.dump(s, file_data, ensure_ascii=False, indent=2)

graphics_final.main()
