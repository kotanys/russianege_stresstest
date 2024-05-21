from random import Random
try:
    import keyboard
except ModuleNotFoundError:
    print('Установите модуль keyboard командой `python -m pip install keyboard`')
    exit(1)

VOWELS = 'аяэеоёиыую'

wordsln = 'облегчЁнный\nпремировАть\nграждАнство\nсверлИт\nкровоточАщий\nободрИть\nэкспЕрт\nкиломЕтр\nкрасИвейший\nобострИть\nмозаИчный\nосвЕдомишься\nподнЯв\nпрожОрлива\nдОверху\nнамЕрение\nквартАл\nнавралА\nбАнты\nвзялА\nзвонИт\nвероисповЕдание\nкОнусов\nщемИт\nоткУпорить\nсорвалА\nсозЫв\nозлОбить\nкормЯщий\nзакУпорив\nнакренИтся\nпрожИвший\nтОртов\nсрЕдства\nсмазлИва\nрвалА\nмонолОг\nдецимЕтр\nнормировАть\nнекролОг\nпрИняли\nбаловАть\nсантимЕтр\nнизведЁнный\nоблилАсь\nвоссоздалА\nприбылА\nнанЯвшийся\nнавЕрх\nперелилА\nзакУпорить\nснялА\nнефтепровОд\nзАняло\nслИвовый\nразбаловАть\nеретИк\nизбаловАть\nдозИровать\nзАняли\nотключЁнный\nмиллимЕтр\nзвалА\nналилА\nгазопровОд\nдосУг\nстолЯр\nсирОты\nкаталОг\nнарвалА\nсОгнутый\nвключИшь\nновостЕй\nполилА\nкиоскЁр\nслИва\nкровоточИть\nИксы\nпрИнятый\nбухгАлтеров\nкрасИвее\nнОготь\nоблегчИть\nсверлИшь\nположИл\nободрИшься\nсорИт\nпослАла\nплодоносИть\nцЕнтнер\nдоЯр\nнадорвалАсь\nнОвости\nцемЕнт\nкремнЯ\nклАла\nвключЁн\nдокумЕнт\nнарОст\nщЁлкать\nпонялА\nприручЁнный\nоблегчИт\nненадОлго\nнЕдруг\nдобралА\nводопровОд\nтОрты\nзАнял\nзАгодя\nподелЁнный\nобнялАсь\nжилОсь\nначАвший\nнасорИт\nвключЁнный\nчЕрпать\nотозвалА\nлОктя\nклЕить\nлыжнЯ\nсвЁкла\nвключИм\nободрЁнный\nаэропОрты\nпрИбыло\nкорЫсть\nтамОжня\nнадОлго\nуглубИть\nзвонИть\nсуетлИва\nоклЕить\nпортфЕль\nпризЫв\nубралА\nнОгтя\nдозвонИтся\nкУхонный\nвернА\nбОроду\nоткУпорил\nгналА\nотбылА\nконтролЁр\nисчЕрпать\nоптОвый\nпонЯв\nизбалОванный\nпОручни\nвлилАсь\nнЕнависть\nназвалАсь\nшофЁр\nлилА\nшколЯр\nждалА\nчЕлюстей\nлилАсь\nзавИдно\nотозвалАсь\nдефИс\nпрозорлИва\nубыстрИть\nотзЫв (посла)\nпозвалА\nвключИт\nбаловАться\nпОчестей\nпринялА\nнажитА\nдОсуха\nповторИт\nкрАны\nпломбировАть\nзАтемно\nжалюзИ\nдонЕльзя\nлгалА\nмЕстностей\nдозвонЯтся\nнедУг\nлЕкторов\nзапломбировАть\nловкА\nобогналА\nдобралАсь\nмолЯщий\nкремЕнь\nбалОванный\nотдалА\nзАсветло\nтУфля\nпринУдить\nободралА\nпартЕр\nдиспансЕр\nзнАчимость\nзапертА\nдиалОг\nвоспринялА\nмусоропровОд\nотдАв\nдоговорЁнность\nнаделИт\nОтрочество\nобзвонИть\nперезвонИть\nповторЁнный\nнАчал\nперезвонИт\nдобелА\nкОнусы\nопОшлить\nгналАсь\nвзялАсь\nпрИбыл\nбралАсь\nболтлИва\nопределЁн\nлЕкторы\nдовезЁнный\nцепОчка\nприбЫв\nпридАное\nмалЯр\nначАвшись\nстАтуя\nсортировАть'
words = list(set(wordsln.split('\n')))

print('Орфоэпический тренажёр. Чтобы дать ответ, нажмите цифру. Нажмите Ctrl+C, чтобы выйти.\n')

rng = Random()
score, total = 0, 0
errors = set()
try:
    
    last_pressed: int | None = None
    def digit_press_handler(event: keyboard.KeyboardEvent):
        if not event.name or event.name == '0' or not event.name.isdigit():
            return
        global last_pressed
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
            pass

        print(last_pressed, end='')
        valid = last_pressed == correct
        total += 1
        
        if valid:
            print(' ВЕРНО')
            score += 1
            errors.discard(test_word)
        else:
            print(f' НЕВЕРНО. {test_word}')
            errors.add(test_word)
        print(flush=True)
        
        last_pressed = None
except KeyboardInterrupt:
    print('\nВаши ошибки:')
    for word in sorted(errors):
        print(' ', word)
    print(f'Ваш счёт: {score}/{total}')