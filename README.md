# Fitness tracker

Tracker get training data and calculate results of training

Test data:

[('SWM', [720, 1, 80, 25, 40]), ('RUN', [15000, 1, 75]), ('WLK', [9000, 1, 75, 180]),]

*SWM* = Swimming(action, duration, weight, length_pool, count_pool)

*RUN* = Running(action, duration, weight)

*WLK* = SportWalking(action, duration, weight, height)

### Experiments with python OOP

Project has the follow classes:

**Training** - parent class for all trainings, get parameters (action, duration, weight), has methods: get_distance, get_mean_speed, get_spend_calories, show_training_info

**Running(Training)** - change method get_spend_calories

**SportWalking(Training)** - has additional param 'height' and change method get_spend_calories

**Swimming(Training)** - has additional params 'length_pool' and 'count_pool' and own methods get_mean_speed and get_spend_calories

**InfoMessage** - this class create a result message

### PyTests

The project is covered by tests almost for 100%

### Type Hints

All function and classes with annotation

##### Yandex Practicum