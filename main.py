from __future__ import annotations

from typing import Protocol


class HasTrainingMethods(Protocol):
    def get_distance(self) -> float: ...
    def get_mean_speed(self) -> float: ...
    def get_spent_calories(self) -> float: ...
    def show_training_info(self) -> InfoMessage: ...


class Training:
    pass


class Running(Training):
    pass


class SportsWalking(Training):
    pass


class Swimming(Training):
    pass


class InfoMessage:
    pass


def main(training: HasTrainingMethods):
    pass


def read_package(workout_type: str, data: list[int]) -> HasTrainingMethods:
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
