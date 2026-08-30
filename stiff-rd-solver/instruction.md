# Stiff two-species reaction-diffusion simulation

You are given a stiff coupled PDE system modelling two species that diffuse and rapidly exchange mass.

## Governing equations

On the domain x in [0, 1], t in [0, T]:

    du/dt = D * d2u/dx2 + k * (v - u)
    dv/dt = D * d2v/dx2 + k * (u - v)

Boundary conditions (Dirichlet, both fields):

    u(0, t) = u(1, t) = 0
    v(0, t) = v(1, t) = 0

Initial conditions (discontinuous steps):

    u(x, 0) = 1 for 0.2 <= x < 0.6, else 0
    v(x, 0) = 1 for 0.5 <= x < 0.9, else 0

All parameter values (D, k, T) are in /app/params.json. Read them from that file; do not assume them.

## What you must produce

Write the file /app/profile.csv containing the numerical solution at time T.

Format requirements:

1. First line is the header: x,u,v
2. Exactly 501 data rows, for x_i = i / 500 with i = 0, 1, ..., 500, in increasing order.
3. Each row contains x, u(x, T), v(x, T) as decimal floats.
4. Boundary rows must satisfy the Dirichlet conditions (u = v = 0 at x = 0 and x = 1).

## Accuracy requirement

Your solution must match the true solution of the continuous PDE at time T with an absolute error of at most 1e-4 in each field at every grid point. The grading reference is independent of any method: stability and convergence are your responsibility. Note that the exchange term is stiff; choose your time stepping and spatial resolution accordingly and verify convergence yourself (for example by resolution refinement).

You have 14400 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
