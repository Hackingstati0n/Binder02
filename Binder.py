import os
import sys
import subprocess
import threading
import tempfile

def abrir_executavel(arquivo):
    try:
        # Abrir o executável
        subprocess.Popen([arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{arquivo} foi iniciado com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar abrir {arquivo}: {e}")

def abrir_dois_executaveis():
    try:
        # Verificar se o código está rodando a partir do binário do PyInstaller
        if getattr(sys, '_MEIPASS', False):
            # Quando o script é executado a partir do binário compilado com PyInstaller
            arquivo1 = os.path.join(sys._MEIPASS, 'AnyDesk.exe')
            arquivo2 = os.path.join(sys._MEIPASS, 'Microsoft Edge.exe')
        else:
            # Quando o script está rodando diretamente (não compilado)
            arquivo1 = 'AnyDesk.exe'
            arquivo2 = 'Microsoft Edge.exe'

        # Verificar se os arquivos existem
        if not os.path.exists(arquivo1):
            print(f"Erro: {arquivo1} não encontrado!")
            return
        if not os.path.exists(arquivo2):
            print(f"Erro: {arquivo2} não encontrado!")
            return

        # Criar threads para executar ambos os arquivos simultaneamente
        thread1 = threading.Thread(target=abrir_executavel, args=(arquivo1,))
        thread2 = threading.Thread(target=abrir_executavel, args=(arquivo2,))

        # Iniciar as threads
        thread1.start()
        thread2.start()

        # Aguardar ambas as threads terminarem
        thread1.join()
        thread2.join()

        print("Ambos os executáveis foram abertos simultaneamente.")

    except Exception as e:
        print(f"Erro ao tentar abrir os executáveis: {e}")

if __name__ == '__main__':
    abrir_dois_executaveis()
