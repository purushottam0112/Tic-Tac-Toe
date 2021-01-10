########################## Method 1 #################################
# a = ["_", "_", "_", "_", "_", "_","_", "_", "_"]

# b = [[], ["", a[6], a[3], a[0]], ["", a[7], a[4], a[1]], ["", a[8], a[5], a[2]] ]

# print("-----------")
# print("| {} {} {} |".format(a[0], a[1], a[2]))
# print("| {} {} {} |".format(a[3], a[4], a[5]))
# print("| {} {} {} |".format(a[6], a[7], a[8]))
# print("-----------")

# count = 1


# def take_input():
#     coordinate = input("Enter the coordinates! ").split()
#     if len(coordinate[0]) > 1 or len(coordinate[1]) > 1:
#         print("You should inter number!")
#         take_input()
#     else:  
#         fill(x = coordinate[0], y = coordinate[1]) 

# def fill(x, y):
#     global count
#     if x == "0" or x >= "4" or y == "0" or y >= "4":
#         print("Coordinates should be from 1 to 3! ") 
#         return take_input()

#     else:
#         if b[int(x)][int(y)] == "X" or b[int(x)][int(y)] == "O":
#             print("This cell is occupied! Choose another one!")
#             return take_input()
#         else:
#             if count % 2 != 0:
#                 b[int(x)][int(y)] = "X"  
#                 count += 1
                

#             elif count % 2 == 0:
#                 b[int(x)][int(y)] = "O"  
#                 count += 1   
                
                
#             print("-----------")
#             print("| {} {} {} |".format(b[1][3], b[2][3], b[3][3]))
#             print("| {} {} {} |".format(b[1][2], b[2][2], b[3][2]))
#             print("| {} {} {} |".format(b[1][1], b[2][1], b[3][1]))
#             print("-----------")
#             return check_win()
            
# def check_win():
#     for n in range(1, 4):
#         if count <= 10:
#             if b[1][n] == b[2][n] == b[3][n] == "O" or b[1][n] == b[2][n] == b[3][n] == "X" :
#                 p = b[1][n]
#                 print(p,"wins")
#                 return
    
#             elif b[n][1] == b[n][2] == b[n][3] == "O" or b[n][1] == b[n][2] == b[n][3] == "X":
#                 p = b[n][1]
#                 print(p,"wins")
#                 return
    
#             elif b[1][1] == b[2][2] == b[3][3] == "O" or b[1][1] == b[2][2] == b[3][3] == "X":
#                 p = b[1][1]
#                 print(p, "wins")
#                 return
    
#             elif b[1][3] == b[2][2] == b[3][1] == "O" or b[1][3] == b[2][2] == b[3][1] == "X":
#                 p = b[1][3]
#                 print(p, "wins")
#                 return
#             if count == 10:
#                 print("Draw")
#                 return
    
#     take_input()
            
        

# coordinate = input("Enter the coordinates! ").split()
# if len(coordinate[0]) > 1 or len(coordinate[1]) > 1:
#     print("You should inter number!")
#     take_input()
# else:  
#     fill(x = coordinate[0], y = coordinate[1]) 
    
    
    
################ Method 2 ###################
b = [[],["", " ", " ", " "], [""," ", " ", " "], ["", " ", " ", " "]]
print("---------")
print("| {} {} {} |".format(b[1][1], b[1][2], b[1][3]))
print("| {} {} {} |".format(b[2][1], b[2][2], b[2][3]))
print("| {} {} {} |".format(b[3][1], b[3][2], b[3][3]))
print("---------")
count = 1
start = " "
while count <= 9:
    coordinate = input('Enter the coordinates: ').split()
    if coordinate[0].isnumeric() != True or coordinate[1].isnumeric() != True:
        print('You should enter numbers!')
    elif int(coordinate[0]) > 3 or int(coordinate[0]) == 0 or int(coordinate[1]) > 3 or int(coordinate[1]) == 0:
        print('Coordinates should be from 1 to 3!')

    elif b[int(coordinate[0])][int(coordinate[1])] == "X" or b[int(coordinate[0])][int(coordinate[1])] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if count % 2 != 0:    
            b[int(coordinate[0])][int(coordinate[1])]  = "X"
            count += 1
        else:
            b[int(coordinate[0])][int(coordinate[1])]  = "O"
            count += 1


        print("---------")
        print("| {} {} {} |".format(b[1][1], b[1][2], b[1][3]))
        print("| {} {} {} |".format(b[2][1], b[2][2], b[2][3]))
        print("| {} {} {} |".format(b[3][1], b[3][2], b[3][3]))
        print("---------")
    
    columb_row = [any([b[1][n] == b[2][n] == b[3][n] == "X" or b[1][n] == b[2][n] == b[3][n] == "O" or b[n][1] == b[n][2] == b[n][3] == "X" or b[1][n] == b[2][n] == b[3][n] == "O"]) for n in range(1, 4)]

    cross = [b[1][1] == b[2][2] == b[3][3] == 'X' or b[1][1] == b[2][2] == b[3][3] == 'O' or b[1][3] == b[2][2] == b[3][1] == "X" or b[1][3] == b[2][2] == b[3][1] == "O"]

    if any(columb_row):
        start = "finish"
        break
    elif any(cross):
        start = "finish"
        break
            
if start == "finish":
    print(f"{b[int(coordinate[0])][int(coordinate[1])]} wins")
else:
    print('Draw')    

  
    



    

