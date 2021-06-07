import threading


def test_function(argument):
    print(f'function: {argument}')


my_task = threading.Thread(target=test_function, args=(10, ))
my_task.start()
