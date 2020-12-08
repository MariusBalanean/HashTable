import random


def creeaza_CNP(S, AA, LL, ZZ, JJ, NNN, C):
    """
    Descrie un dictionar
    :param S:
    :param AA:
    :param LL:
    :param ZZ:
    :param JJ:
    :param NNN:
    :param C:
    :return:
    """
    return {
        'S': S,
        'AA': AA,
        'LL': LL,
        'ZZ': ZZ,
        'JJ': JJ,
        'NNN': NNN,
        'C': C
    }


def get_S(CNP):
    return CNP['S']


def get_AA(CNP):
    return CNP['AA']


def get_LL(CNP):
    return CNP['LL']


def get_ZZ(CNP):
    return CNP['ZZ']


def get_JJ(CNP):
    return CNP['JJ']


def get_NNN(CNP):
    return CNP['NNN']


def get_C(CNP):
    return CNP['C']


def genereaza_valori():
    S = random.randint(5, 6)  # alege intre 5 si 6

    AA = random.randint(0, 20)  # alege intre 0 si 20 o valoare INT
    if AA < 10:
        a1 = 0
        a2 = AA
    else:
        a1 = AA // 10
        a2 = AA % 10

    LL = random.randint(1, 12)
    if LL < 10:
        l1 = 0
        l2 = LL
    else:
        l1 = LL // 10
        l2 = LL % 10

    ZZ = None
    if AA in [4, 8, 12, 16, 20]:
        if LL == 2:
            ZZ = random.randint(1, 29)
    else:
        if LL == 2:
            ZZ = random.randint(1, 28)
    if ZZ is None:
        if LL in [1, 3, 5, 7, 9, 11]:
            ZZ = random.randint(1, 31)
        else:
            ZZ = random.randint(1, 30)
    if ZZ < 10:
        z1 = 0
        z2 = ZZ
    else:
        z1 = ZZ // 10
        z2 = ZZ % 10

    JJ = random.randint(1, 52)
    if JJ < 10:
        j1 = 0
        j2 = JJ
    else:
        j1 = JJ // 10
        j2 = JJ % 10

    NNN = random.randint(1, 999)
    if NNN < 10:
        n1 = 0
        n2 = 0
        n3 = NNN
    elif NNN < 100:
        n1 = 0
        n2 = NNN // 10
        n3 = NNN % 10
    else:
        n1 = NNN // 100
        n2 = NNN // 10
        n3 = NNN % 10

    C = 2 * S + 7 * a1 + 9 * a2 + 1 * l1 + 4 * l2 + 6 * z1 + 3 * z2 + 5 * j1 + 8 * j2 + 2 * n1 + 7 * n2 + 9 * n3
    r = C % 11
    if r < 10:
        C = r
    else:
        C = 1
    lst_valori = [S, AA, LL, ZZ, JJ, NNN, C]
    return lst_valori


def valori_to_string():
    lst_valori = genereaza_valori()
    S = lst_valori[0]
    AA = lst_valori[1]
    LL = lst_valori[2]
    ZZ = lst_valori[3]
    JJ = lst_valori[4]
    NNN = lst_valori[5]
    C = lst_valori[6]
    S = str(S)
    if AA < 10:
        AA = f'0{str(AA)}'
    else:
        AA = str(AA)
    if LL < 10:
        LL = f'0{str(LL)}'
    else:
        LL = str(LL)
    if ZZ < 10:
        ZZ = f'0{str(ZZ)}'
    else:
        ZZ = str(ZZ)
    if JJ < 10:
        JJ = f'0{str(JJ)}'
    else:
        JJ = str(JJ)
    if NNN < 10:
        NNN = f'00{str(NNN)}'
    elif NNN < 100:
        NNN = f'0{str(NNN)}'
    else:
        NNN = str(NNN)
    C = str(C)
    CNP = creeaza_CNP(S, AA, LL, ZZ, JJ, NNN, C)
    return CNP


def CNP_to_string():
    CNP = valori_to_string()
    CNP_str = f'{get_S(CNP)}{get_AA(CNP)}{get_LL(CNP)}{get_ZZ(CNP)}{get_JJ(CNP)}{get_NNN(CNP)}{get_C(CNP)}'
    CNP_int = int(CNP_str)
    return CNP_int


lst_CNP = []
for x in range(0, 1000):
    CNP = CNP_to_string()
    if CNP not in lst_CNP:
        lst_CNP.append(CNP)


with open('CNP.txt', 'w') as file:
    file.write(f'{lst_CNP}')
