def BastShoe(command: str) -> str:
    
    global string_now, all_strings, undo

    if command[0] not in ['1','2','3','4','5']:
        return string_now
    
    if command[0] == '1':
        if len(undo) > 0:
            undo = []
            all_strings = [string_now]
        string_now += command[2:]
        all_strings.append(string_now)
    
    if command[0] == '2':
        if len(undo) > 0:
            undo = []
            all_strings = [string_now]
        string_now = string_now[:-int(command[2:])]
        all_strings.append(string_now)
    
    if command[0] == '3':
        if int(command[2:]) > len(string_now)-1:
            return ''
        string_now = string_now[int(command[2:])]
    
    if command[0] == '4':
        if len(all_strings) > 1:
            all_strings.pop(-1)
            string_now = all_strings[-1]
            undo.append(string_now)
            

    if command[0] == '5':
        if len(undo) > 0:
            undo.pop(-1)
            string_now = undo[-1]
            
    
string_now = ''
all_strings = ['']
undo = []

