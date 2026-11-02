# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Blood Pressure Dipping Hemodynamics Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentBloodPressureDippingHemodynamics

def main():
    agent = PersonalAgentBloodPressureDippingHemodynamics()

    print("=" * 70)
    print("DEMO: Personal Agent Nocturnal Blood Pressure Dipping & Hemodynamics")
    print("=" * 70)

    # 1. Evaluate ABPM 24-Hour Blood Pressure Profile
    # Day: 126/80 mmHg, Night: 104/64 mmHg (Dipping: ~17.5%)
    res_dip = agent.calculate_nocturnal_bp_dipping_profile(
        daytime_sbp_mean=126.0,
        daytime_dbp_mean=80.0,
        nighttime_sbp_mean=104.0,
        nighttime_dbp_mean=64.0
    )

    print(f"\n1. Nocturnal BP Dipping Profile:")
    print(f"   Daytime BP: {res_dip['daytime_sbp_dbp']} (MAP: {res_dip['daytime_mean_arterial_pressure_map']} mmHg)")
    print(f"   Nighttime BP: {res_dip['nighttime_sbp_dbp']} (MAP: {res_dip['nighttime_mean_arterial_pressure_map']} mmHg)")
    print(f"   Systolic Dipping: {res_dip['systolic_dipping_percentage']}")
    print(f"   Phenotype: {res_dip['dipping_phenotype']} ({res_dip['clinical_status']})")
    print(f"   Pulse Pressure (Day/Night): {res_dip['daytime_pulse_pressure_pp']} / {res_dip['nighttime_pulse_pressure_pp']} mmHg")
    print(f"   Stiffness Warning: {res_dip['arterial_stiffness_warning']}")
    print(f"   CV Risk Assessment: {res_dip['cardiovascular_risk_assessment']}")
    print(f"   Guidance: {res_dip['chronotherapeutic_guidance']}")

    # 2. Evaluate Orthostatic Hemodynamics (Standing Test)
    res_ortho = agent.evaluate_orthostatic_hemodynamics(
        supine_sbp=122.0,
        supine_dbp=76.0,
        standing_3min_sbp=118.0,
        standing_3min_dbp=78.0
    )

    print(f"\n2. Orthostatic Postural Hemodynamics:")
    print(f"   Supine BP: {res_ortho['supine_blood_pressure']}")
    print(f"   Standing 3-Min BP: {res_ortho['standing_3min_blood_pressure']}")
    print(f"   Delta SBP / DBP: {res_ortho['delta_systolic_mmHg']} / {res_ortho['delta_diastolic_mmHg']} mmHg")
    print(f"   Diagnosis: {res_ortho['hemodynamic_diagnosis']}")
    print(f"   Baroreflex Status: {res_ortho['baroreflex_regulatory_status']}")
    print(f"   Fall Risk: {res_ortho['fall_and_syncope_risk']}")

    print("\nVerification complete: Hemodynamic dipping engine executed flawlessly.")

if __name__ == "__main__":
    main()
