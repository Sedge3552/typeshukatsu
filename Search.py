def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 探索範囲の先頭のインデックス
    left = 0
    # 探索範囲の末端のインデックス
    right = len(sorted_array) - 1

    # 探索範囲が無くなるまで対象を探索
    while left <= right:
        # 探索範囲の中間のインデックス
        midle = (left + right) // 2
        # 探索対象が探索範囲の中央の値よりも小い場合、探索範囲を前半分に絞って再度探索
        if target_number < sorted_array[midle]:
            right = midle - 1
            continue
        # 探索対象が探索範囲の中央の値よりも大きい場合、探索範囲を後半分に絞って再度探索
        if target_number > sorted_array[midle]:
            left = midle + 1
            continue
        # 探索対象が見つかった場合、そのインデックスを返却
        if target_number == sorted_array[midle]:
            return midle
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()