from trainings_classes import (InfoMessage, Running, SportsWalking, Swimming,
                               Training)


def test_training_class():
    training = Training(1000, 2.5, 95)
    assert training.M_IN_KM == 1000
    assert training.LEN_STEP == 0.68
    assert training.action == 1000
    assert training.duration == 2.5
    assert training.weight == 95
    distance = training.get_distance()
    assert distance == 0.68
    mean_speed = training.get_mean_speed()
    assert mean_speed == 0.272
    assert hasattr(training, 'get_spend_calories')
    obj_message = training.show_training_info()
    assert type(obj_message) == InfoMessage


def test_running_class():
    running = Running(50000, 2.5, 95)
    assert running.M_IN_KM == 1000
    assert running.LEN_STEP == 0.68
    assert running.action == 50000
    assert running.duration == 2.5
    assert running.weight == 95
    distance = running.get_distance()
    assert distance == 34
    mean_speed = running.get_mean_speed()
    assert mean_speed == 13.6
    calories = running.get_spend_calories()
    assert calories == 53.39
    obj_message = running.show_training_info()
    assert type(obj_message) == InfoMessage


def test_walking_class():
    walking = SportsWalking(25000, 2.5, 95, 180)
    assert walking.M_IN_KM == 1000
    assert walking.LEN_STEP == 0.68
    assert walking.action == 25000
    assert walking.duration == 2.5
    assert walking.weight == 95
    assert walking.height == 180
    distance = walking.get_distance()
    assert distance == 17
    mean_speed = walking.get_mean_speed()
    assert mean_speed == 6.8
    calories = walking.get_spend_calories()
    assert calories == 8.3125
    obj_message = walking.show_training_info()
    assert type(obj_message) == InfoMessage


def test_swimming_class():
    swimming = Swimming(1000, 1.5, 95, 25, 40)
    assert swimming.M_IN_KM == 1000
    assert swimming.LEN_STEP == 1.38
    assert swimming.action == 1000
    assert swimming.duration == 1.5
    assert swimming.weight == 95
    assert swimming.length_pool == 25
    assert swimming.count_pool == 40
    distance = swimming.get_distance()
    assert distance == 1.38
    mean_speed = swimming.get_mean_speed()
    assert round(mean_speed, 3) == 0.667
    calories = swimming.get_spend_calories()
    assert round(calories, 3) == 335.667
    obj_message = swimming.show_training_info()
    assert type(obj_message) == InfoMessage


def test_infomessage_class():
    info_message = InfoMessage('Running', 34, 2.5, 13.6, 53.39)
    assert info_message.training_type == 'Running'
    assert info_message.distance == 34
    assert info_message.duration == 2.5
    assert info_message.speed == 13.6
    assert info_message.calories == 53.39
    message = info_message.get_message()
    assert type(message) == str
