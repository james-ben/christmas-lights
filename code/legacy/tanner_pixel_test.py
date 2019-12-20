from time import sleep
import board
import neopixel

# print(board.__dict__)

pins = [
    # board.D1, 
    # board.D2, 
    # board.D3, 
    # board.D4, 
    # board.D5, 
    # board.D6, 
    # board.D7, 
    # board.D8, 
    # board.D9, 
    # board.D10, 
    # board.D11, 
    # board.D12, 
    # board.D13, 
    # board.D14, 
    # board.D15, 
    # board.D16, 
    # board.D17, 
    board.D18, 
    # board.D19, 
    # board.D20, 
    # board.D21, 
    # board.D22, 
    # board.D23, 
    # board.D24, 
    # board.D25, 
    # board.D26, 
    # board.D27, 
    # board.D28, 
    # board.D29, 
    # board.D30, 
    # board.D31, 
    # board.D32, 
    # board.D33, 
    # board.D34, 
    # board.D35, 
    # board.D36, 
    # board.D37, 
    # board.D38, 
    # board.D39, 
    # board.D40, 
]

for pin in pins:
    try:
        print(pin)
        pixels = neopixel.NeoPixel(pin, 30)
        pixels[0] = (255, 0, 0)
        pixels[1] = (0, 255, 0)
        del pixels
        sleep(1)
    except:
        print("Nope")