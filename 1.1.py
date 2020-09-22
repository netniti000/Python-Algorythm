std_list = [6,2,3,7,9]
print("初期値: ", std_list)

x = std_list[2]
print("stdlist[2] = : ", x)

std_list.append(99)
print("要素の追加後: ", std_list)

std_list.insert(3,10)
print("要素の挿入後: ",std_list)

std_list.pop(3)
print("要素の削除後: ",std_list)
