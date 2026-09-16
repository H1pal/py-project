from pynput.keyboard import Controller, Key, Listener

keyList = {
  Key.alt: False,
  Key.ctrl: False
}

controller = Controller()
is_typing = False  # 재귀(무한루프) 방지 플래그
# 터미널에 keyboard가 출력되고 다시 입력되어 무한 루프가 발생함

def on_press(key):
  global is_typing

  if is_typing:
      return  # 우리가 만든 합성 입력은 무시
  keyList[key] = True

  is_typing = True 
  if (key not in Key and keyList[Key.ctrl] and keyList[Key.alt]): # ctrl 또는 alt가 눌러져 있는 상태라면
    if (key.char == 's'):
      controller.type('System.out.println();')
  is_typing = False

def on_release(key):
  if (key in Key):
    keyList[key] = False

  if key == Key.esc:
      return False

with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()