import pyautogui
import time

pyautogui.alert("O codigo será executado, não mexa em nada no seu computador até o codigo terminar")
pyautogui.PAUSE = 1

# Abrir o navegador e entrar no google drive
pyautogui.press('winleft')
pyautogui.write('Brave')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/u/2/my-drive')
pyautogui.press('enter')

# Clicar no arquivo e arrastar ele até o drive 
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1662, 279)
pyautogui.mouseDown()
pyautogui.moveTo(503, 399)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()

# Esperar 5 segundos
time.sleep(3)

pyautogui.alert("O codigo acabou pode usar o computador novamente")