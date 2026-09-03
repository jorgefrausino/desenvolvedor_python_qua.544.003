import pyautogui as auto
from datetime import date
def abrir_cmd():
    auto.press("win")
    auto.write("cmd")
    auto.press("enter")


def hoje():
    return date.today().strftime("%d/%m/y%")

def main():
    auto.PAUSE = 0.75
    abrir_cmd()
    auto.write(r'cd C:\Users\ALUNO\Jorge\desenvolvedor_python_qua.544.003\Desenvolvedor Python.QUA.544.003')
    auto.press("enter")
    auto.write(r"git add .")
    auto.press("enter")
    auto.write(r'git commit -m "{hoje()}"')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")
    auto.write("exit")
    auto.press("enter")


if __name__ == "__main__":
    main()
