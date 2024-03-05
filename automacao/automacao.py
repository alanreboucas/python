#modules
import pyautogui
import time
import pandas
#vars
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#code
pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.PAUSE = 2
pyautogui.write("chrome")
pyautogui.PAUSE = 2
pyautogui.press("enter")
pyautogui.PAUSE = 2

# entra no site
pyautogui.write(link)
pyautogui.PAUSE = 2
pyautogui.press("enter")
pyautogui.PAUSE = 2
#pyautogui.click(x=2486, y=473)
pyautogui.press("tab")
pyautogui.PAUSE = 3

# digita Login e senha
pyautogui.write("usuario1@xpto.com")
pyautogui.PAUSE = 1
pyautogui.press("tab")
pyautogui.PAUSE = 1
pyautogui.write("xxxxxxxxxxxxxxx")
pyautogui.PAUSE = 1
pyautogui.press("enter")
# pyautogui.hotkey("ctrl", "c")

# pagina carregada
time.sleep(3)

#importar base de dados
tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    #preenchendo os valores
    pyautogui.PAUSE = 1
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.press("tab")
    pyautogui.write(codigo)

    marca = tabela.loc[linha,"marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

#condicao
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(5)

    #scroll up
    pyautogui.scroll(5000)