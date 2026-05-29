# LTspice Modeling and Analysis of a Marx Generator

This repository contains the LTspice simulation and performance analysis of a multi-stage Marx Generator. The project focuses on generating standardized lightning impulse voltages (1.2/50 μs) and evaluating the waveform distortions under varying load conditions.

## 📌 Project Overview
In high-voltage engineering, standard impulse waves are critical for testing insulation reliability. This project models a 3-stage Marx Generator and compares the simulated outputs against the theoretical double-exponential mathematical model and the **IEC 60060-1** standard tolerances.

### Key Objectives:
* Design an operational Marx Generator circuit in LTspice.
* Extract and analyze the front time ($T_1$) and tail time ($T_2$).
* Observe the effects of high capacitive and low ohmic loading on the wave shape.
* Validate the results using theoretical curve fitting.

## 🗂️ Repository Structure
* `/simulation`: Contains the `.asc` LTspice schematic files.
* `/data`: Exported raw data and measurement logs from the transient analysis.
* `/scripts`: Python scripts for evaluating theoretical vs. simulated curve fitting.
* `/docs`: Circuit diagrams and the final academic report.

## 🛠️ Tools & Technologies
* **LTspice:** For circuit modeling and transient simulation.
* **Python (NumPy/Matplotlib):** For data visualization and calculating the Root Mean Square Error (RMSE) between theoretical and simulated curves.

## 📊 Results Summary
The simulation was tested under three main scenarios:
1. **Ideal Load (1 nF):** Compliant with front time ($T_1$) standards.
2. **High Capacitive Load (5 nF):** Results in a delayed wave front, exceeding IEC limits.
3. **Low Ohmic Load (1000 Ω):** Causes premature discharge, drastically shortening the wave tail ($T_2$).

Detailed graphical comparisons and mathematical proofs can be found in the `docs/report.pdf` file.
