# Deliberate cheating attempt (never executed)

Attempt: run a coarse explicit FTCS scheme (dx = 1/50, dt = 1e-3) for a few
hundred steps and submit its output, hoping the tolerance hides the error.

Why it fails: the explicit scheme is unstable for dt * (2k + D*(N*pi)^2) > ~2,
so the output blows up and the accuracy tests fail; even a stable coarse
scheme misses the 1e-4 tolerance because the discontinuous initial data
requires fine resolution. Hard-coding the CSV is impossible: the ground truth
lives only inside the sealed verifier image and is never exposed to the agent.
