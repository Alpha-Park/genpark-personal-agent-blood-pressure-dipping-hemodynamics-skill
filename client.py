# -*- coding: utf-8 -*-
"""Personal Agent Blood Pressure Dipping Hemodynamics Skill.

Zero-dependency Ambulatory Blood Pressure Monitoring (ABPM) nocturnal dipping modeler,
mean arterial pressure (MAP) calculator, and orthostatic hemodynamic risk evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentBloodPressureDippingHemodynamics:
    """Quantitative ambulatory blood pressure dipping and vascular hemodynamics modeler
    based on the American Heart Association (AHA) and European Society of Hypertension (ESH) guidelines."""

    def calculate_nocturnal_bp_dipping_profile(
        self,
        daytime_sbp_mean: float = 124.0,
        daytime_dbp_mean: float = 78.0,
        nighttime_sbp_mean: float = 108.0,
        nighttime_dbp_mean: float = 66.0
    ) -> Dict[str, Any]:
        """Calculates nocturnal systolic dipping percentage, Mean Arterial Pressure (MAP),
        Pulse Pressure (PP), and cardiovascular risk tier."""
        day_sbp = max(70.0, float(daytime_sbp_mean))
        day_dbp = max(40.0, float(daytime_dbp_mean))
        night_sbp = max(60.0, float(nighttime_sbp_mean))
        night_dbp = max(35.0, float(nighttime_dbp_mean))

        # Systolic Dipping Percentage = (1 - (Night SBP / Day SBP)) * 100
        systolic_dipping_pct = round((1.0 - (night_sbp / day_sbp)) * 100.0, 1)
        diastolic_dipping_pct = round((1.0 - (night_dbp / day_dbp)) * 100.0, 1)

        # Dipping Phenotype Classification
        if systolic_dipping_pct > 20.0:
            phenotype = "Extreme Dipper"
            cv_risk = "Elevated risk of nocturnal cerebral ischemia, hypoperfusion, and anterior ischemic optic neuropathy"
            clinical_status = "Sub-optimal: excessive nocturnal hypotension"
        elif systolic_dipping_pct >= 10.0:
            phenotype = "Normal Dipper"
            cv_risk = "Optimal cardiovascular risk profile; physiological nocturnal autonomic down-regulation"
            clinical_status = "Physiologically optimal entrainment"
        elif systolic_dipping_pct >= 0.0:
            phenotype = "Non-Dipper"
            cv_risk = "Moderately elevated risk of left ventricular hypertrophy, microalbuminuria, and stroke"
            clinical_status = "Sub-clinical autonomic failure or elevated nighttime sympathetic tone"
        else:
            phenotype = "Reverse Dipper (Riser)"
            cv_risk = "Highest hazard ratio for cardiovascular mortality, congestive heart failure, and renal disease"
            clinical_status = "Severe circadian hemodynamic dysregulation (Nocturnal Hypertension)"

        # Mean Arterial Pressure: MAP = DBP + 1/3(SBP - DBP)
        day_map = round(day_dbp + (day_sbp - day_dbp) / 3.0, 1)
        night_map = round(night_dbp + (night_sbp - night_dbp) / 3.0, 1)

        # Pulse Pressure: PP = SBP - DBP
        day_pp = round(day_sbp - day_dbp, 1)
        night_pp = round(night_sbp - night_dbp, 1)
        large_artery_stiffness_flag = day_pp > 60.0 or night_pp > 55.0

        return {
            "daytime_sbp_dbp": f"{day_sbp}/{day_dbp} mmHg",
            "nighttime_sbp_dbp": f"{night_sbp}/{night_dbp} mmHg",
            "systolic_dipping_percentage": f"{systolic_dipping_pct}%",
            "diastolic_dipping_percentage": f"{diastolic_dipping_pct}%",
            "dipping_phenotype": phenotype,
            "clinical_status": clinical_status,
            "cardiovascular_risk_assessment": cv_risk,
            "daytime_mean_arterial_pressure_map": day_map,
            "nighttime_mean_arterial_pressure_map": night_map,
            "daytime_pulse_pressure_pp": day_pp,
            "nighttime_pulse_pressure_pp": night_pp,
            "arterial_stiffness_warning": large_artery_stiffness_flag,
            "chronotherapeutic_guidance": (
                "Consider evening dosing of antihypertensives or magnesium taurate to restore physiological nocturnal dipping."
                if systolic_dipping_pct < 10.0 else
                "Maintain circadian sleep hygiene and balanced sodium-potassium intake."
            )
        }

    def evaluate_orthostatic_hemodynamics(
        self,
        supine_sbp: float = 120.0,
        supine_dbp: float = 76.0,
        standing_3min_sbp: float = 114.0,
        standing_3min_dbp: float = 78.0
    ) -> Dict[str, Any]:
        """Evaluates Orthostatic Hypotension (OH) or Orthostatic Hypertension
        following 3 minutes of quiet standing."""
        delta_sbp = round(standing_3min_sbp - supine_sbp, 1)
        delta_dbp = round(standing_3min_dbp - supine_dbp, 1)

        # Classical Consensus Criteria for Orthostatic Hypotension:
        # SBP drop >= 20 mmHg OR DBP drop >= 10 mmHg within 3 min
        is_orthostatic_hypotension = delta_sbp <= -20.0 or delta_dbp <= -10.0
        # Orthostatic Hypertension: SBP rise >= 20 mmHg
        is_orthostatic_hypertension = delta_sbp >= 20.0

        if is_orthostatic_hypotension:
            diagnosis = "Orthostatic Hypotension Confirmed"
            baroreflex_status = "Impaired baroreflex mediated vasoconstriction or relative intravascular volume depletion"
        elif is_orthostatic_hypertension:
            diagnosis = "Orthostatic Hypertension Confirmed"
            baroreflex_status = "Hyperactive sympathetic adrenergic vasoconstrictive reflex"
        else:
            diagnosis = "Normative Orthostatic Hemodynamics"
            baroreflex_status = "Intact arterial baroreceptor reflex and peripheral vascular capacitance"

        return {
            "supine_blood_pressure": f"{supine_sbp}/{supine_dbp} mmHg",
            "standing_3min_blood_pressure": f"{standing_3min_sbp}/{standing_3min_dbp} mmHg",
            "delta_systolic_mmHg": delta_sbp,
            "delta_diastolic_mmHg": delta_dbp,
            "hemodynamic_diagnosis": diagnosis,
            "baroreflex_regulatory_status": baroreflex_status,
            "fall_and_syncope_risk": "Elevated" if is_orthostatic_hypotension else "Low"
        }
