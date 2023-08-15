import keyboard
import math, time, os

def draw(c):
    mx = max(c, key=lambda q: q[0])[0]
    my = max(c, key=lambda q: q[1])[1]
    for y in range(my + 1):
        line = ""
        for x in range(mx + 1):
            if (x, y) in c:
                line += "$"
            else:
                line += " "
        print(line)

# Create the object's initial coordinates
obj_x, obj_y = 1, 2

c1 = [(50, k) for k in range(0, 25)]
c2 = [(k, 25) for k in range(50, 100)]
c3 = [(100, k) for k in range(0, 26)]

# Function to move the object
def move_object():
    global obj_x, obj_y, x1, y1
    while True:
        if keyboard.is_pressed('w'):
            obj_y -= 1
        if keyboard.is_pressed('a'):
            obj_x-=1
        if keyboard.is_pressed('s'):
            obj_y += 1
        if keyboard.is_pressed('d'):
            obj_x+=1

        try:
        # Redraw the grid with the updated object position
            if obj_x>0 and obj_y>0 and obj_y<50 and obj_x<190:
                draw([(round(obj_x), round(obj_y))]+c1+c2+c3)
                time.sleep(0.05)
                os.system("clear")
        except KeyboardInterrupt:
            break
        
move_object()

