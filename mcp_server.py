# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Blood Pressure Dipping Hemodynamics Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentBloodPressureDippingHemodynamics

mcp = FastMCP("PersonalAgentBloodPressureDippingHemodynamics")
client = PersonalAgentBloodPressureDippingHemodynamics()

@mcp.tool()
def calculate_nocturnal_bp_dipping_profile(
    daytime_sbp_mean: float = 124.0,
    daytime_dbp_mean: float = 78.0,
    nighttime_sbp_mean: float = 108.0,
    nighttime_dbp_mean: float = 66.0
) -> str:
    """Calculates nocturnal systolic dipping percentage, Mean Arterial Pressure (MAP), and phenotype."""
    import json
    return json.dumps(client.calculate_nocturnal_bp_dipping_profile(
        daytime_sbp_mean, daytime_dbp_mean, nighttime_sbp_mean, nighttime_dbp_mean
    ), indent=2)

@mcp.tool()
def evaluate_orthostatic_hemodynamics(
    supine_sbp: float = 120.0,
    supine_dbp: float = 76.0,
    standing_3min_sbp: float = 114.0,
    standing_3min_dbp: float = 78.0
) -> str:
    """Evaluates Orthostatic Hypotension (OH) or Orthostatic Hypertension across 3 minutes standing."""
    import json
    return json.dumps(client.evaluate_orthostatic_hemodynamics(
        supine_sbp, supine_dbp, standing_3min_sbp, standing_3min_dbp
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
