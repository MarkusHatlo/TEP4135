from __future__ import annotations
import attrs

import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import scipy.integrate


def differential_equation(
    time: float, y_values: list[npt.NDArray[np.float64]], beta: float
) -> list[float]:
    """
    Coupled first order ODE system describing the Falkner-Skan problem
    """
    dxdt = [
        y_values[1],
        y_values[2],
        -y_values[0] * y_values[2] - beta * (1 - y_values[1] ** 2),
    ]

    return dxdt


@attrs.define
class IVPSolver:
    """
    Solves the Falkner-Skan initial value problem for a given
    range of eta values. The solver itself takes a value for
    beta, and an initial guess f_init for the solver
    """

    eta_max: float
    eta_eval: npt.NDArray[np.float64] = attrs.field(init=False)

    def __attrs_post_init__(self):
        """
        Create the "time" vector for the evaluation, in this case it is eta
        """
        self.eta_eval = np.linspace(0.0, self.eta_max, 25)

    def solve(self, beta: float, f_init: list[float]) -> IVPSolution:
        solution = scipy.integrate.solve_ivp(
            differential_equation,
            t_span=[0.0, self.eta_max],
            y0=f_init,
            t_eval=self.eta_eval,
            args=[beta],
        )

        f = solution.y[0, :]
        f_derivative = solution.y[1, :]
        f_double_derivative = solution.y[2, :]
        eta = solution.t

        return IVPSolution(f, f_derivative, f_double_derivative, eta)


@attrs.define
class IVPSolution:
    """
    Solution of the Falkner-Skan initial value problem
    """

    f: npt.NDArray[np.float64]
    f_derivative: npt.NDArray[np.float64]
    f_double_derivative: npt.NDArray[np.float64]
    eta: npt.NDArray[np.float64]


# NOTE: Use this function in your codes
# You can call it by first importing this file from the same folder
# as your script using the command:
#
# import falkner_skan
#
# and then you can call the solver for a value of beta with
#
# falkner_skan.solver(beta)
def solver(beta: float) -> IVPSolution:
    """
    Solves the Falkner-Skan initial value problem for a given value of beta
    """
    d2_f0_1 = 0.3
    d2_f0_2 = 2
    # NOTE: Don't set this too high!
    # eta_max > 7 results in rapidly changing solutions,
    # which takes the ODE solver a long time to compute
    eta_max = 5
    solver = IVPSolver(eta_max=eta_max)

    # First point of shooting-secant method
    f_init1 = [0, 0, d2_f0_1]
    sol1 = solver.solve(beta, f_init1)

    for loop_counter in range(50):
        # Second point for secant method
        f_init2 = [0, 0, d2_f0_2]
        sol2 = solver.solve(beta, f_init2)

        # Extract info for secant method
        f1 = sol1.f_derivative[-1]
        f2 = sol2.f_derivative[-1]

        # Check whether we have converged
        f_exact = 1.0
        shoot_error = abs(f_exact - f2)
        accept = 1e-6
        # Break when converged
        if abs(shoot_error) < accept:
            print(f"Converged in {loop_counter} iterations")
            return sol2

        g3 = (d2_f0_1 * (f2 - f_exact) - d2_f0_2 * (f1 - f_exact)) / (f2 - f1)
        d2_f0_1 = d2_f0_2
        d2_f0_2 = g3

        sol1 = sol2

        # print("iteration %03d:  F''''(0) =%.7f  error = %.2e\n" % (i_ctr, d2_f0_2, shoot_error))

    # If we did not converge, return the last solution
    return sol1


if __name__ == "__main__":
    sol = solver(beta=10.0 * np.pi / 2.0)
    plt.plot(sol.eta, sol.f_derivative)
    plt.show()
