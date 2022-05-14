def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # ソート後の配列の格納場所
    sorted_array = []
    # 配列の先頭のインデックス
    head_index = 0
    # 配列の末端のインデックス
    tail_index = len(array) - 1

    # 先頭と末端の検索がぶつかるまで配列をソート
    while tail_index != head_index:
        # 先頭から基準値以上の要素が見つかるまで検索
        while array[head_index] < pivot:
            # 末端の検索とぶつかった場合、検索終了
            if tail_index == head_index:
                break
            head_index += 1
        # 末端から基準値未満の要素が見つかるまで検索
        while array[tail_index] >= pivot:
            # 先頭の検索とぶつかった場合、検索終了
            if tail_index == head_index:
                break
            tail_index -= 1
        # 先頭からの探索と末端からの探索の両方で要素が見つかった場合、見つかった要素を入れ替える
        else:
            array[head_index], array[tail_index] = array[tail_index], array[head_index]
    
    # 配列に基準値未満の要素が含まれない場合、基準値だけのグループと基準値より大きいグループに分ける
    if head_index == 0:
        head_index += 1
    
    # 基準値未満だったグループをソート
    sorted_array.extend(sort(array[ : head_index]))
    # 基準値以上だったグループをソート
    sorted_array.extend(sort(array[head_index : ]))

    # ソート後の配列を返却
    return sorted_array

    # ここまで記述

if __name__ == '__main__':
    main()