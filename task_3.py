import types
import os
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        # Получаем текущее время
        now = datetime.datetime.now()
        
        # Вызываем оригинальную функцию и получаем её результат
        result = old_function(*args, **kwargs)
        
        # Подготавливаем данные для записи в лог
        log_message = (
            f"{now} - Function '{old_function.__name__}' was called\n"
            f"Arguments: args={args}, kwargs={kwargs}\n"
            f"Returned: {result}\n\n"
        )
        
        # Записываем данные в файл
        with open('main.log', 'a') as log_file:
            log_file.write(log_message)
        
        return result
    
    return new_function

@logger
def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item

def test_2():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()
