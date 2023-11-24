from datetime import datetime

def sveiciens(pasreizeja_stunda):
    if 6 <= pasreizeja_stunda < 12:
        return "labrīt"
    elif 12 <= pasreizeja_stunda < 18:
        return "labdien"
    else:
        return "labvakar"

def aka():
    pašreizējā_laiks = datetime.now()
    pašreizējā_stunda = pašreizējā_laiks.hour

    print(sveiciens(pašreizējā_stunda))

aka()
