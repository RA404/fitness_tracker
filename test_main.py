try:
    import main
except ModuleNotFoundError:
    assert False, 'Module main not found'


try:
    import trainings_classes
except ModuleNotFoundError:
    assert False, 'Module trainings_classes not found'


def test_main():
    running_object = trainings_classes.Running(15000, 1, 75)
    assert main.main(running_object) == (
        'Тип тренировки: Running; '
        'Длительность: 1 ч.; '
        'Дистанция: 10.2 км; '
        'Ср. скорость: 10.2 км/ч; '
        'Потрачено ккал: 12.27.'
    )
    running_object1 = trainings_classes.Running(15000, 1.5, 75)
    assert main.main(running_object1) == (
        'Тип тренировки: Running; '
        'Длительность: 1.5 ч.; '
        'Дистанция: 10.2 км; '
        'Ср. скорость: 6.8 км/ч; '
        'Потрачено ккал: 11.52.'
    )
    swimming_object = trainings_classes.Swimming(720, 1, 80, 25, 40)
    assert main.main(swimming_object) == (
        'Тип тренировки: Swimming; '
        'Длительность: 1 ч.; '
        'Дистанция: 0.994 км; '
        'Ср. скорость: 1.0 км/ч; '
        'Потрачено ккал: 336.0.'
    )
    walking_object = trainings_classes.SportsWalking(9000, 1, 75, 180)
    assert main.main(walking_object) == (
        'Тип тренировки: Sport walking; '
        'Длительность: 1 ч.; '
        'Дистанция: 6.12 км; '
        'Ср. скорость: 6.12 км/ч; '
        'Потрачено ккал: 2.625.'
    )
