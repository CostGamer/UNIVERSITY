def greeting(language, times):
    dc = {'English': 'Hello',
          'Chineese': '你好',
          'Russian': 'Привет'}

    gr = dc.get(language, 0)
    if gr != 0:
        for _ in range(times):
            print(gr)
    else:
        print('Choose the appropriate language')


language = input('Write the language(English, Chineese, Russian): ')
times = int(input('Write the digit: '))

greeting(language, times)
