list_rating = [7, 4, 3, 3, 2]
new_elem = int(input('Введите число: '))

for num in range(len(list_rating)):
    print(num)
    if list_rating[num] < new_elem:
        list_rating.insert(num, new_elem)
        break
    elif num == len(list_rating) - 1:
        list_rating.append(new_elem)
        break
print(list_rating)
