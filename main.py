from random import Random
from typing import Literal, Callable
import codecs
try:
    import keyboard
except ModuleNotFoundError:
    print('Установите модуль keyboard командой `python -m pip install keyboard`')
    exit(1)


Event = Literal['correct', 'wrong', 'wait']
VOWELS = 'аяэеоёиыую'

def main(event_handler: None | Callable[[Event], None] = None):
    if not event_handler:
        def mock(event): pass
        event_handler = mock
    
    with codecs.open('words.txt', 'r', 'utf8') as f:
        words = list(set(map(lambda s: s.strip(), f.readlines())))

    print('Орфоэпический тренажёр. Чтобы дать ответ, нажмите цифру. Нажмите Ctrl+C, чтобы выйти.\n')

    rng = Random()
    score, total = 0, 0
    errors = set()

    try:
        last_pressed: int | None = None
        def digit_press_handler(event: keyboard.KeyboardEvent):
            if not event.name or event.name == '0' or not event.name.isdigit():
                return
            nonlocal last_pressed
            last_pressed = int(event.name)
        keyboard.on_release(digit_press_handler)

        while True:
            test_word = rng.choice(words)
            correct, vowel_count = 0, 0
            ptrs = '       '
            for c in test_word:
                if c == '(':
                    break
                if c.lower() not in VOWELS:
                    ptrs += ' '
                    continue
                vowel_count += 1
                ptrs += str(vowel_count)
                if c.isupper():
                    correct = vowel_count
            if correct == 0:
                continue
            
            print(f"Слово: {test_word.lower().replace('ё', 'е')}")
            print(ptrs, flush=True)
            while not last_pressed or last_pressed > vowel_count:
                event_handler('wait')

            print(last_pressed, end='')
            valid = last_pressed == correct
            total += 1

            if valid:
                event_handler('correct')
                score += 1
                errors.discard(test_word)
                print(' ВЕРНО')
            else:
                event_handler('wrong')
                errors.add(test_word)
                print(f' НЕВЕРНО. {test_word}')
            print(flush=True)

            last_pressed = None
    except KeyboardInterrupt:
        print('\nВаши ошибки:')
        for word in sorted(errors):
            print(' ', word)
        print(f'Ваш счёт: {score}/{total}')
        
if __name__ == '__main__':
    main()