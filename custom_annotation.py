from __future__ import annotations

from typing import Protocol

from trainings_classes import InfoMessage


class SubTraining(Protocol):
    def get_distance(self) -> float:
        ...

    def get_mean_speed(self) -> float:
        ...

    def show_training_info(self) -> InfoMessage:
        ...
