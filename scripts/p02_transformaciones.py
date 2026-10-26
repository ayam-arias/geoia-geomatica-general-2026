"""Práctica 2 · Transformaciones entre PSAD56 y SIRGAS-Chile.

Uso:  python scripts/p02_transformaciones.py
"""
from pathlib import Path
import pandas as pd
from pyproj import CRS, Transformer

RAIZ = Path(__file__).resolve().parents[1]
df = pd.read_csv(RAIZ / "data" / "puntos_control_santiago.csv")

t_utm = Transformer.from_crs("EPSG:5360", "EPSG:5361", always_xy=True)
df["E_sirgas2002"], df["N_sirgas2002"] = t_utm.transform(df.lon.values, df.lat.values)

t_psad = Transformer.from_crs("EPSG:5361", "EPSG:24879", always_xy=True)
df["E_psad56"], df["N_psad56"] = t_psad.transform(df.E_sirgas2002.values, df.N_sirgas2002.values)
df["dE"] = df.E_psad56 - df.E_sirgas2002
df["dN"] = df.N_psad56 - df.N_sirgas2002

utm19_2025 = CRS.from_proj4("+proj=utm +zone=19 +south +ellps=GRS80 +units=m +no_defs")
try:
    t25 = Transformer.from_crs("EPSG:11473", utm19_2025, always_xy=True)
    df["E_2025"], df["N_2025"] = t25.transform(df.lon.values, df.lat.values)
except Exception as exc:  # base EPSG antigua
    print("EPSG:11473 no disponible en esta instalación de PROJ:", exc)

pd.set_option("display.width", 160)
print(df.drop(columns=["descripcion"]).round(2).to_string(index=False))
