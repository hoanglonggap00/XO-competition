data_player_1 = []
data_player_2 = []
linh1 = 0
linh2 = 0



def check_Ox(data):
    for i in range(len(data) - 4):
        if int(data[i][0]) + 1 == int(data[i + 1][0]) and int(data[i + 1][0]) + 1 == int(data[i + 2][0]) and int(data[i + 2][0]) + 1 == int(data[i + 3][0]) and int(data[i + 3][0]) + 1 == int(data[i + 4][0]):
            linh1 = i
            return True
            break
        else:
            return False


def check_Oy(data):
    for j in range(len(data) - 4):
        if int(data[j][1]) + 1 == int(data[j + 1][1]) and int(data[j + 1][1]) + 1 == int(data[j + 2][1]) and int(data[j + 2][1]) + 1 == int(data[j + 3][1]) and int(data[j + 3][1]) + 1 == int(data[j + 4][1]):
            linh2 = j
            return True
            break
        else:
            return False



def check_one_line_Ox(data):
    if data[linh1][0] == data[linh1 + 1][0] and data[linh1 + 1][0] == data[linh1 + 2][0] and data[linh1 + 2][0] == data[linh1 + 3][0] and data[linh1 + 3][0] == data[linh1 + 4][0]:
        return True


def check_one_line_Oy(data):
    if data[linh2][1] == data[linh2 + 1][1] and data[linh2 + 1][1] == data[linh2 + 2][1] and data[linh2 + 2][1] == data[linh2 + 3][1] and data[linh2 + 3][1] == data[linh + 4][1]:
        return True


def check_win(data):
    if check_Ox(data) and check_Oy(data):
        return True
    elif check_Oy(data) and check_one_line_Ox(data):
        return True
    elif check_Ox(data) and check_one_line_Oy(data):
        return True


def check_x_already_there(x, data1, data2):
    if x in data1 or x in data2:
        return True


while True:
    x1 = input('X: ').split(' ')
    if x1:
        while check_x_already_there(x1, data_player_1, data_player_2) == True:
            print("vi tri da dc danh")
            x1 = input("X: ").split(' ')
    data_player_1.append(x1)
    if check_win(data_player_1):
        print("X win")
        break

    x2 = input('O: ').split(' ')
    if x2:
        while check_x_already_there(x2, data_player_2, data_player_1) == True:
            print("vi tri da dc danh")
            x2 = input("O: ").split(' ')
    data_player_2.append(x2)
    if check_win(data_player_2):
        print("O win")
        break