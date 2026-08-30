import csv
import math
import os

D = 0.02
K = 150.0
T = 0.1
M = 2000
N = 500
TOL = 1e-4
PATH = "/app/profile.csv"


def sine_coeffs(a, b):
    return [
        2.0 * (math.cos(m * math.pi * a) - math.cos(m * math.pi * b)) / (m * math.pi)
        for m in range(1, M + 1)
    ]


def reference_solution():
    cu = sine_coeffs(0.2, 0.6)
    cv = sine_coeffs(0.5, 0.9)
    xs = [i / N for i in range(N + 1)]
    u_ref = [0.0] * (N + 1)
    v_ref = [0.0] * (N + 1)
    for m in range(1, M + 1):
        mu = D * (m * math.pi) ** 2
        ep = math.exp(-mu * T)
        if ep < 1e-12:
            break
        eq = math.exp(-(mu + 2.0 * K) * T)
        wp = 0.5 * (cu[m - 1] + cv[m - 1])
        zm = 0.5 * (cu[m - 1] - cv[m - 1])
        au = wp * ep + zm * eq
        av = wp * ep - zm * eq
        for i, x in enumerate(xs):
            s = math.sin(m * math.pi * x)
            u_ref[i] += au * s
            v_ref[i] += av * s
    return xs, u_ref, v_ref


XS, U_REF, V_REF = reference_solution()


def load_profile():
    assert os.path.exists(PATH), "artifact /app/profile.csv is missing"
    with open(PATH, newline="") as f:
        rows = list(csv.DictReader(f))
    return rows


def test_file_format_and_grid():
    rows = load_profile()
    assert len(rows) == N + 1, f"expected {N + 1} rows, got {len(rows)}"
    for i, r in enumerate(rows):
        assert abs(float(r["x"]) - XS[i]) <= 1e-12, f"row {i}: wrong x value"
    assert abs(float(rows[0]["u"])) <= 1e-12 and abs(float(rows[0]["v"])) <= 1e-12
    assert abs(float(rows[-1]["u"])) <= 1e-12 and abs(float(rows[-1]["v"])) <= 1e-12


def test_u_accuracy():
    rows = load_profile()
    err = max(abs(float(r["u"]) - U_REF[i]) for i, r in enumerate(rows))
    assert err <= TOL, f"max absolute u error {err:.3e} exceeds {TOL:.0e}"


def test_v_accuracy():
    rows = load_profile()
    err = max(abs(float(r["v"]) - V_REF[i]) for i, r in enumerate(rows))
    assert err <= TOL, f"max absolute v error {err:.3e} exceeds {TOL:.0e}"
