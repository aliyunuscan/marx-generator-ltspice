import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Load Data
try:
    data = np.loadtxt('3asamaliSenaryo1.txt', skiprows=1)
except FileNotFoundError:
    print("Error: Please ensure the '3asamaliSenaryo1.txt' file is in the same directory as this script.")
    exit()

t = data[:, 0]  
V = data[:, 1] 

# 2. Catch the start of the pulse 
start_idx = np.argmax(V > 100) # Consider the pulse started when voltage exceeds 100V
t_pulse = t[start_idx:] - t[start_idx] # Shift the time axis to start at 0
V_pulse = V[start_idx:]

# 3. Mathematical constants for the ideal 1.2/50 µs standard lightning impulse
alpha = 14600      # Tail damping constant (T2)
beta = 2.73e6      # Front rising constant (T1)

def theoretical_wave(t, V0):
    return V0 * (np.exp(-alpha * t) - np.exp(-beta * t))

# 4. Curve Fitting
# Using your measured 22.54 kV (22544 V) as the initial guess for V0
popt, pcov = curve_fit(theoretical_wave, t_pulse, V_pulse, p0=[22544])
V0_fitted = popt[0]

# Calculate the theoretical wave using the fitted V0
V_theoretical = theoretical_wave(t_pulse, V0_fitted)

# 5. RMSE (Root Mean Square Error) Calculation
rmse = np.sqrt(np.mean((V_pulse - V_theoretical)**2))
rmse_percent = (rmse / np.max(V_pulse)) * 100

# 6. Plotting the Graph
plt.figure(figsize=(10, 6))
plt.plot(t_pulse * 1e6, V_pulse / 1000, label='LTspice Simulation (Marx Generator)', linewidth=3, color='#1f77b4')
plt.plot(t_pulse * 1e6, V_theoretical / 1000, label='Theoretical Double Exponential Equation', linestyle='--', linewidth=2.5, color='#d62728')

plt.title('Marx Generator Impulse Voltage: Simulation vs. Theoretical Curve', fontsize=14, fontweight='bold')
plt.xlabel('Time ($\mu$s)', fontsize=12)
plt.ylabel('Voltage (kV)', fontsize=12)
plt.xlim(-5, 120) # Focus on the most critical part of the waveform
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

# Add text box with fitting results and RMSE
text_str = f"Calculated V0 Coefficient: {V0_fitted/1000:.2f} kV\nDeviation (RMSE): {rmse_percent:.2f} %"
plt.text(60, 15, text_str, fontsize=12, bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()

print(f"INFO: Curve fitting completed successfully. RMSE Error: {rmse_percent:.2f} %")