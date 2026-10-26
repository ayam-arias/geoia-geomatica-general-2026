"""Práctica 6 · Exactitud posicional según NSSDA (FGDC, 1998)."""
from pathlib import Path
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
df = pd.read_csv(RAIZ / "data" / "checkpoints_ejemplo.csv")
dx, dy, dz = (df.E_producto - df.E_ref, df.N_producto - df.N_ref, df.H_producto - df.H_ref)
rx, ry, rz = (np.sqrt(np.mean(d ** 2)) for d in (dx, dy, dz))
rr = np.hypot(rx, ry)
print(f"n = {len(df)}")
print(f"Sesgo: E={dx.mean():+.3f} N={dy.mean():+.3f} H={dz.mean():+.3f} m")
print(f"RMSEx={rx:.3f} RMSEy={ry:.3f} RMSEr={rr:.3f} RMSEz={rz:.3f} m")
print(f"Exactitud horizontal 95 % = {1.7308 * rr:.3f} m")
print(f"Exactitud vertical   95 % = {1.9600 * rz:.3f} m")
