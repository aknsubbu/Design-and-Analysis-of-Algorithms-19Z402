import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbolic variables
n, omega = sp.symbols('n omega')
j = sp.I

# Define the unit step function
u = sp.Heaviside(n, 0)

def plot_dtft(x_n, n_min, n_max, title):
    """Calculate and plot the DTFT of a given signal."""
    try:
        if n_max == sp.oo or n_min == -sp.oo:
            # Handling cases with infinite summation bounds
            X_omega = sp.Sum(x_n * sp.exp(-j * omega * n), (n, n_min, n_max)).doit()
        else:
            X_omega = sp.summation(x_n * sp.exp(-j * omega * n), (n, n_min, n_max))

        X_omega = sp.simplify(X_omega)
        
        X_omega_func = sp.lambdify(omega, X_omega, 'numpy')
        omega_range = np.linspace(-2*np.pi, 2*np.pi, 400)
        X_omega_vals = X_omega_func(omega_range)
        
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))
        
        ax[0].plot(omega_range, np.abs(X_omega_vals))
        ax[0].set_title('Magnitude of ' + title)
        ax[0].set_xlabel('ω')
        ax[0].set_ylabel('|X(ω)|')
        ax[0].grid(True)
        
        ax[1].plot(omega_range, np.angle(X_omega_vals))
        ax[1].set_title('Phase of ' + title)
        ax[1].set_xlabel('ω')
        ax[1].set_ylabel('∠X(ω)')
        ax[1].grid(True)
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting {title}: {e}")

x1 = [0, 1, 2, 1, 0]
x1_expr = sum(x1[i] * sp.KroneckerDelta(n, i) for i in range(len(x1)))
print("Plotting X1(ω)")
plot_dtft(x1_expr, 0, len(x1)-1, 'X1(ω)')

x2 = (1/8)**n * u
print("Plotting X2(ω)")
plot_dtft(x2, 0, sp.oo, 'X2(ω)')

x3 = (1/8)**(n+2) * u
print("Plotting X3(ω)")
plot_dtft(x3, 0, sp.oo, 'X3(ω)')

x4 = (1/8)**(-n) * sp.Heaviside(-n, 0)
print("Plotting X4(ω)")
plot_dtft(x4, -sp.oo, 0, 'X4(ω)')

x5 = (1/8)**n * sp.Heaviside(n-2, 0)
print("Plotting X5(ω)")
plot_dtft(x5, 2, sp.oo, 'X5(ω)')
