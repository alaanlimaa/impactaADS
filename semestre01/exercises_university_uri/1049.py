p1 = str(input()).lower().strip()
if p1 == 'vertebrado':
    p2 = str(input()).lower().strip()
    if p2 == 'ave':
        p3 = str(input()).lower().strip()
        if p3 == 'carnivoro':
            print('aguia')
        if p3 == 'onivoro':
            print('pomba')
    if p2 == 'mamifero':
        p3 = str(input()).lower().strip()
        if p3 == 'onivoro':
            print('homem')
        if p3 == 'herbivoro':
            print('vaca')
if p1 == 'invertebrado':
    p2 = str(input()).lower().strip()
    if p2 == 'inseto':
        p3 = str(input()).lower().strip()
        if p3 == 'hematofago':
            print('pulga')
        if p3 == 'herbivoro':
            print('lagarta')
    if p2 == 'anelideo':
        p3 = str(input()).lower().strip()
        if p3 == 'hematofago':
            print('sanguessuga')
        if p3 == 'onivoro':
            print('minhoca')




