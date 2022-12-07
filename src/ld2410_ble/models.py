from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LD2410BLEState:

    is_moving: bool = False
    is_static: bool = False
    moving_target_distance: int = 0
    moving_target_energy: int = 0
    static_target_distance: int = 0
    static_target_energy: int = 0
    detection_distance: int = 0
    max_motion_gates: int = 8
    max_static_gates: int = 8
    motion_energy_gates: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    static_energy_gates: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]