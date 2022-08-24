def formula():

    print('이차방정식은 ax^2 + bx + c의 형태입니다.')
    a = float(input('a의 값을 입력해주세요'))
    b = float(input('b의 값을 입력해주세요'))
    c = float(input('c의 값을 입력해주세요'))

    if a == 0:
        print('a의 값은 0이 될 수 없습니다.')
        formula()

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-1 * b + d**0.5) / (2*a)
        x2 = (-1 * b - d**0.5) / (2*a)
        print('x = ',x1,'또는 x = ',x2)

    elif d == 0:
        x = (-1 * b + d**0.5) / (2*a)
        print('x = ',x,'(중근)')

    else:
        x1 = (-1 * b + d**0.5) / (2*a)
        x2 = (-1 * b - d**0.5) / (2*a)
        print('x = ',x1,'또는 x = ',x2)

formula()
