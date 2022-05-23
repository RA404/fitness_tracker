from __future__ import annotations


class Training:
    LEN_STEP = 0.68
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        distance: float = self.get_distance()
        return distance / self.duration

    def get_spend_calories(self) -> float:
        pass

    def show_training_info(self) -> InfoMessage:
        training_type: str = "General training"
        if isinstance(self, Running):
            training_type = "Running"
        elif isinstance(self, Swimming):
            training_type = "Swimming"
        elif isinstance(self, SportsWalking):
            training_type = "Sport walking"

        distance: float = self.get_distance()
        duration: float = self.duration
        speed: float = self.get_mean_speed()
        calories: float = self.get_spend_calories()
        info_message: InfoMessage = InfoMessage(
            training_type, distance, duration, speed, calories
        )
        return info_message


class Running(Training):
    def get_spend_calories(self) -> float:
        coeff_calorie_1: int = 18
        coeff_calorie_2: int = 20
        mean_speed: float = self.get_mean_speed()
        return (
            (coeff_calorie_1 * mean_speed * coeff_calorie_2)
            * self.weight
            / self.M_IN_KM
            * self.duration
        )


class SportsWalking(Training):
    def __init__(
        self, action: int, duration: float, weight: float, height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spend_calories(self) -> float:
        coeff_calorie1: float = 0.35
        coeff_calorie2: float = 0.29
        mean_speed: float = self.get_mean_speed()
        return (
            coeff_calorie1 * self.weight
            + (mean_speed ** 2 // self.height) * coeff_calorie2 * self.weight
        ) * self.duration


class Swimming(Training):
    LEN_STEP = 1.38

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: int,
        count_pool: int,
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spend_calories(self) -> float:
        coeff_calorie1: float = 1.1
        coeff_calorie2: int = 2
        mean_speed: float = self.get_mean_speed()
        return (mean_speed + coeff_calorie1) * coeff_calorie2 * self.weight


class InfoMessage:
    def __init__(
        self,
        training_type: str,
        distance: float,
        duration: float,
        speed: float,
        calories: float,
    ) -> None:
        self.training_type = training_type
        self.distance = distance
        self.duration = duration
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (
            f"Тип тренировки: {self.training_type}; "
            f"Длительность: {str(round(self.duration, 3))} ч.; "
            f"Дистанция: {str(round(self.distance, 3))} км; "
            f"Ср. скорость: {str(round(self.speed, 3))} км/ч; "
            f"Потрачено ккал: {str(round(self.calories, 3))}."
        )