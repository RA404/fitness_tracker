from __future__ import annotations

from typing import List, Optional

from custom_annotation import SubTraining
from trainings_classes import InfoMessage, Running, SportsWalking, Swimming


def main(training: Optional[SubTraining]):
    if training is None:
        return "Unexpected type of training!"
    info: InfoMessage = training.show_training_info()
    message: str = info.get_message()
    return message


def read_package(workout_type: str, data: List[int]) -> Optional[SubTraining]:
    action: int = data[0]
    duration: float = data[1]
    weight: float = data[2]
    height: float = 0
    length_pool: int = 0
    count_pool: int = 0
    if workout_type == "WLK":
        height = data[3]
    elif workout_type == "SWM":
        length_pool = data[3]
        count_pool = data[4]

    workout_types = {
        "SWM": Swimming(action, duration, weight, length_pool, count_pool),
        "RUN": Running(action, duration, weight),
        "WLK": SportsWalking(action, duration, weight, height),
    }

    if workout_type in workout_types:
        training: SubTraining = workout_types[workout_type]
        return training
    else:
        return None


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        print(main(training))
