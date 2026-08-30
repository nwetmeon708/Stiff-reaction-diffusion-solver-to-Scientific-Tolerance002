import json
import math

with open("/app/params.json") as f:
    P = json.load(f)

D = P["D"]
K = P["k"]
T = P["T"]
ua, ub = P["u_step"]
va, vb = P["v_step"]
N = P["output_points"] - 1
M = 2000


def sine_coeffs(a, b):
    return [
        2.0 * (math.cos(m * math.pi * a) - math.cos(m * math.pi * b)) / (m * math.pi)
        for m in range(1, M + 1)
    ]


cu = sine_coeffs(ua, ub)
cv = sine_coeffs(va, vb)

lines = ["x,u,v"]
for i in range(N + 1):
    x = i / N
    u = 0.0
    v = 0.0
    for m in range(1, M + 1):
        mu = D * (m * math.pi) ** 2
        ep = math.exp(-mu * T)
        if ep < 1e-12:
            break
        eq = math.exp(-(mu + 2.0 * K) * T)
        wp = 0.5 * (cu[m - 1] + cv[m - 1])
        zm = 0.5 * (cu[m - 1] - cv[m - 1])
        s = math.sin(m * math.pi * x)
        u += (wp * ep + zm * eq) * s
        v += (wp * ep - zm * eq) * s
    lines.append(f"{x:.17g},{u:.17g},{v:.17g}")

with open("/app/profile.csv", "w") as f:
    f.write("\n".join(lines) + "\n")

print("reference profile written to /app/profile.csv")
