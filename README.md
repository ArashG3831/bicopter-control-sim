# Bicopter Attitude Control (Simulink)

Short, review-friendly repo for our **bicopter attitude control** study. The project compares **Lead** and **PID** controllers on linearized attitude dynamics and then checks behavior on the **nonlinear** plant.

---

## What this repo contains
- **docs/** — Simulink models + one MATLAB helper script and reference papers
- **figs/** — images used in the report/presentation (step responses, block diagrams, etc.)
- **presentation.pptx** — slide deck
- **report.pdf** — final write‑up

### Layout
```
.
├─ docs/
│  ├─ ControlSimulation.slx
│  ├─ nonlinearFinal.slx
│  ├─ Compensator.m
│  ├─ Modeling_and_attitude_control_of_Bi-copter.pdf
│  ├─ DesignofaRoboticBicopter_IEEE_08988694.pdf
│  └─ paper_refrence.pdf
├─ figs/
│  └─ (PNG/SVG figures used in the report & slides)
├─ presentation.pptx
└─ report.pdf
```

---

## Requirements
- **MATLAB & Simulink** (R2022a or newer recommended)
- Control System Toolbox (for linear analysis/tuning)

---

## Quickstart
1. **Nonlinear plant**  
   Open `docs/nonlinearFinal.slx` and run a small‑angle hover test to verify the plant.

2. **Linearized control loop**  
   Open `docs/ControlSimulation.slx` to run step and disturbance tests on the **linear** attitude channel(s).

3. **Controller design**  
   Use `docs/Compensator.m` as a scratchpad to:
   - extract/define a linear model around hover,
   - design a **Lead** or **PID** controller to your target rise‑time/overshoot,
   - update gains back into `ControlSimulation.slx` and re‑run.

4. **Figures**  
   Save generated plots into **figs/** (the slides and report expect figures from here).

---

## Notes
- **Lead** gives low overshoot but shows **steady‑state error** under step disturbances (type‑0).  
- **PID/PI** removes steady‑state error but can increase overshoot unless tuned carefully (consider derivative filtering and anti‑windup).  
- Expect differences when the same controller is applied to the **nonlinear** model (coupling, saturation).

---

## Next steps
- Add actuator/motor limits and anti‑windup blocks to the Simulink models.  
- Export Bode/root‑locus/step plots automatically to **figs/** from `Compensator.m`.  
- Try an LQR/LQG design for coupled axes.

