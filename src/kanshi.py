import pyautogui

# 始点と終点の座標を基にして、その範囲内の画像をクリップボードに保存する
def check_red_in_clipboard_image(start_x, start_y, end_x, end_y):

    width = end_x - start_x
    height = end_y - start_y

    im = pyautogui.screenshot(region=(start_x, start_y, width, height))
    im.save("aaa.png")
    for x in range(im.width):
        for y in range(im.height):
            r, g, b = im.getpixel((x, y))
            if 206 <= r <= 217 and 138 <= g <= 148 and 138 <= b <= 145:
               
                return True
    return False

# 始点と終点の座標を基にして、60秒ごとにポーリングを行う
def poll(start_x, start_y, end_x, end_y):
    return check_red_in_clipboard_image(start_x, start_y, end_x, end_y)