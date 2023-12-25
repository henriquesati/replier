from ast import List
from time import sleep
import pyautogui
import msvcrt
import keyboard
from index import pass_mouse_coord

height = 1080
width = 1980
janela_x = 512
janela_y = 516
def get_mouse_coord():
   mouse_pos = pyautogui.position();
   mouse_pos_x = mouse_pos.x
   mouse_pos_y = mouse_pos.y
   return [mouse_pos_x, mouse_pos_y]

def execute_click(par: list[float]) -> None:
    print(par[0], par[1])
    pyautogui.click(par[0], par[1]) 
    
def execute_m_clicks(par: list[float]):
    for i in range(4):
        execute_click([par[0]+ (i*janela_x), par[1]])
        sleep(0.5)
    for i in range(4):
        execute_click([par[0] + (i*janela_x), par[1]+janela_y])
        sleep(1)

def main():
    while True:
        if keyboard.is_pressed('esc'):
            break;
        if keyboard.is_pressed('x'):
            coord = get_mouse_coord();
            pass_mouse_coord(coord);
            print(coord)
            break;
        # execute_m_clicks(coord);x
        print("Looping...")
        
if __name__ == "__main__":
    main()
    