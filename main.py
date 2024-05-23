from random import Random
from typing import Literal, Callable
import codecs
try:
    import keyboard
except ModuleNotFoundError:
    print('Установите модуль keyboard командой `python -m pip install keyboard`')
    exit(1)


Event = Literal['correct', 'wrong', 'wait']
stop_game_hotkeys: list[str] = ['Ctrl+C', 'Q', 'Esc']
VOWELS = 'аяэеоёиыую'

def main(event_handler: None | Callable[[Event], None] = None):
    if not event_handler:
        def mock(event): pass
        event_handler = mock
    
    with codecs.open('words.txt', 'r', 'utf8') as f:
        words = list(set(map(lambda s: s.strip(), f.readlines())))

    print('Орфоэпический тренажёр. Чтобы дать ответ, нажмите цифру. Нажмите ', end='')
    print(*stop_game_hotkeys, sep=', или ', end='')
    print(', чтобы выйти.', end='\n\n')

    rng = Random()
    score, total = 0, 0
    errors = set()
    
    last_pressed: int | None = None
    def digit_press_handler(digit: int):
        nonlocal last_pressed
        last_pressed = digit
        
    stop_game = False
    def quit_game_handler():
        nonlocal stop_game
        stop_game = True
        
    for hotkey in stop_game_hotkeys:
        keyboard.add_hotkey(hotkey, quit_game_handler, suppress=True)
    for digit in range(1, 10):
        keyboard.add_hotkey(str(digit), digit_press_handler, args=(digit,), suppress=True)

    while not stop_game:
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
            if stop_game:
                break
            event_handler('wait')
        if stop_game:
            break
        
        print(last_pressed, end='')
        valid = last_pressed == correct
        total += 1

        if valid:
            score += 1
            errors.discard(test_word)
            print(' ВЕРНО')
            event_handler('correct')
        else:
            errors.add(test_word)
            print(f' НЕВЕРНО. {test_word}')
            event_handler('wrong')
        print(flush=True)

        last_pressed = None
    
    keyboard.unhook_all_hotkeys()
    print('\nВаши ошибки:')
    for word in sorted(errors):
        print(' ', word)
    print(f'Ваш счёт: {score}/{total}')
        
if __name__ == '__main__':
    main()