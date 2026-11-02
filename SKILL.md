---
name: genpark-personal-agent-blood-pressure-dipping-hemodynamics-skill
version: "1.0.0"
description: "Zero-dependency Ambulatory Blood Pressure Monitoring (ABPM) nocturnal dipping modeler, mean arterial pressure (MAP) calculator, and orthostatic hemodynamic risk evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Blood Pressure Dipping Hemodynamics Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to analyze ambulatory blood pressure hemodynamics, compute nocturnal dipping ratios, classify dipper phenotypes (Extreme, Normal, Non-Dipper, Reverse Dipper), calculate Mean Arterial Pressure (MAP) and Pulse Pressure (PP), and diagnose orthostatic baroreflex stability.

## Agent In-Context Capabilities

- **Nocturnal Dipping Calculation**: Measures percentage drop from daytime mean to nighttime mean, identifying cardiovascular risk phenotypes.
- **Hemodynamic Load Analysis**: Computes MAP ($DBP + \frac{1}{3}PP$) and Pulse Pressure ($SBP - DBP$) to detect large artery stiffening.
- **Orthostatic Baroreflex Testing**: Checks for orthostatic hypotension ($\Delta SBP \le -20$ mmHg or $\Delta DBP \le -10$ mmHg) after 3 minutes standing.

## Tools Summary

1. `calculate_nocturnal_bp_dipping_profile`: Determines dipping percentage, phenotype, and chronotherapeutic recommendations.
2. `evaluate_orthostatic_hemodynamics`: Assesses postural blood pressure adaptations and syncope risk.
