STRING_NOW = ''
ALL_STRINGS = ['']
UNDO = []

def BastShoe(command: str) -> str:

    global STRING_NOW, ALL_STRINGS, UNDO

    if command[0] == '1':
        if len(UNDO) > 0:
            UNDO = []
            ALL_STRINGS = [STRING_NOW]
        STRING_NOW += command[2:]
        ALL_STRINGS.append(STRING_NOW)
        return STRING_NOW

    if command[0] == '2':
        if len(UNDO) > 0:
            UNDO = []
            ALL_STRINGS = [STRING_NOW]
        STRING_NOW = STRING_NOW[:-int(command[2:])]
        ALL_STRINGS.append(STRING_NOW)
        return STRING_NOW

    if command[0] == '3':
        if int(command[2:]) > len(STRING_NOW)-1:
            return ''
        return STRING_NOW[int(command[2:])]

    if command[0] == '4':
        if len(ALL_STRINGS) > 1:
            if not UNDO:
                UNDO.append(STRING_NOW)
            elif UNDO[-1] != STRING_NOW:
                UNDO.append(STRING_NOW)
            ALL_STRINGS.pop()
            STRING_NOW = ALL_STRINGS[-1]
            if UNDO[-1] != STRING_NOW:
                UNDO.append(STRING_NOW)
        return STRING_NOW

    if command[0] == '5':
        if len(UNDO) > 1:
            UNDO.pop()
            STRING_NOW = UNDO[-1]
            if STRING_NOW != ALL_STRINGS[-1]:
                ALL_STRINGS.append(STRING_NOW)
        return STRING_NOW

    return STRING_NOW

