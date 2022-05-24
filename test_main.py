from trainings_classes import Running, SportsWalking, Swimming


try:
    import main
except ModuleNotFoundError:
    assert False, 'Module main not found'


try:
    import trainings_classes
except ModuleNotFoundError:
    assert False, 'Module trainings_classes not found'


def create_main_message(
    type_of_training: str,
    distance: float,
    duration: float,
    mean_speed: float,
    calories_expended: float,
) -> str:
    return (
        f'Type of training: {type_of_training}; '
        f'Duration: {duration} h.; '
        f'Distance: {distance} km; '
        f'Mean speed: {mean_speed} km/h; '
        f'Calories extended: {calories_expended}.'
    )


def test_main():
    running_object = trainings_classes.Running(15000, 1, 75)
    result_message = create_main_message('Running', 10.2, 1, 10.2, 12.27)
    assert main.main(running_object) == result_message
    running_object1 = trainings_classes.Running(15000, 1.5, 75)
    result_message1 = create_main_message('Running', 10.2, 1.5, 6.8, 11.52)
    assert main.main(running_object1) == result_message1

    swimming_object = trainings_classes.Swimming(720, 1, 80, 25, 40)
    result_message = create_main_message('Swimming', 0.994, 1, 1.0, 336.0)
    assert main.main(swimming_object) == result_message

    walking_object = trainings_classes.SportsWalking(9000, 1, 75, 180)
    result_message = create_main_message('Sport walking', 6.12, 1, 6.12, 2.625)
    assert main.main(walking_object) == result_message


def test_read_package():
    result = main.read_package('SWM', [720, 1, 80, 25, 40])
    assert type(result) == Swimming
    result = main.read_package('RUN', [15000, 1, 75])
    assert type(result) == Running
    result = main.read_package('WLK', [9000, 1, 75, 180])
    assert type(result) == SportsWalking
