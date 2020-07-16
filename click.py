import pynput
from pynput.keyboard import Controller, Key, Listener
from pynput.mouse import Button


def on_click(x, y, button, pressed):
    # 实例化键盘
    kb = Controller()

    # 使用键盘输入一个字母
    kb.press(Key.ctrl)
    kb.press(Key.alt)
    kb.press('.')
    kb.release(Key.ctrl)
    kb.release(Key.alt)
    kb.release('.')
    kb.pressed(Key.ctrl,Key.alt,'.')
    if button == Button.right:
        print("关闭")
        return False


# Collect events until released
with pynput.mouse.Listener(
        on_click=on_click,) as listener:
    listener.join()
