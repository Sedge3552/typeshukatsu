for num in range(1, 101):
    string = ''

    # ここから記述

    # 3の倍数の時は出力をFizzに変更
    if num % 3 == 0:
        string += 'Fizz'
    # 5の倍数の時は出力をBuzz、15の倍数の時は出力をFizzBuzzに変更
    if num % 5 == 0:
        string += 'Buzz'
    # 3の倍数でも5の倍数でもないときは出力を数字に変更
    string = string or f'{num}'

    # ここまで記述

    print(string)