```markdown
# Script para Execução Simultânea de Dois Executáveis

Este script Python permite a execução simultânea de dois executáveis (`AnyDesk.exe` e `Microsoft Edge.exe`) utilizando threads. Ele é compatível com execução direta ou após compilação com PyInstaller.

## Estrutura do Script

O script contém as seguintes funcionalidades principais:

1. **Verificação de Ambiente**: Detecta se o script está sendo executado diretamente ou a partir de um binário compilado com PyInstaller.
2. **Execução de Executáveis**: Abre dois executáveis simultaneamente usando threads.
3. **Tratamento de Erros**: Verifica se os arquivos existem e trata possíveis erros durante a execução.

## Requisitos

- Python 3.6 ou superior.
- Os executáveis `AnyDesk.exe` e `Microsoft Edge.exe` devem estar presentes no diretório correto (ou no bundle do PyInstaller, se compilado).

## Como Usar

### 1. Executando o Script Diretamente

Para executar o script diretamente, certifique-se de que os arquivos `AnyDesk.exe` e `Microsoft Edge.exe` estão no mesmo diretório que o script. Em seguida, execute:

```bash
python nome_do_script.py
```

### 2. Compilando com PyInstaller

Para compilar o script em um executável único com PyInstaller, siga os passos abaixo:

1. Instale o PyInstaller (se ainda não tiver instalado):

```bash
pip install pyinstaller
```

2. Compile o script com o seguinte comando:

```bash
pyinstaller --onefile --noconsole --add-data "AnyDesk.exe;." --add-data "Microsoft Edge.exe;." nome_do_script.py
```

3. O executável gerado estará na pasta `dist`. Certifique-se de que os arquivos `AnyDesk.exe` e `Microsoft Edge.exe` estejam no mesmo diretório que o executável compilado.

### 3. Executando o Binário Compilado

Após a compilação, execute o binário gerado. Ele verificará automaticamente se os executáveis estão presentes e os abrirá simultaneamente.

## Detalhes do Código

### Função `abrir_executavel(arquivo)`

- **Descrição**: Abre um executável usando `subprocess.Popen`.
- **Parâmetros**:
  - `arquivo`: Caminho do executável a ser aberto.
- **Comportamento**:
  - Se o executável for aberto com sucesso, exibe uma mensagem de confirmação.
  - Caso contrário, exibe uma mensagem de erro.

### Função `abrir_dois_executaveis()`

- **Descrição**: Verifica o ambiente de execução (direto ou compilado), localiza os executáveis e os abre simultaneamente usando threads.
- **Comportamento**:
  - Verifica se os arquivos `AnyDesk.exe` e `Microsoft Edge.exe` existem.
  - Cria threads para abrir ambos os executáveis.
  - Aguarda a conclusão das threads e exibe uma mensagem de sucesso ou erro.

### Bloco `if __name__ == '__main__':`

- **Descrição**: Ponto de entrada do script. Chama a função `abrir_dois_executaveis()` para iniciar o processo.

## Exemplo de Uso

1. Coloque os arquivos `AnyDesk.exe` e `Microsoft Edge.exe` no mesmo diretório que o script.
2. Execute o script:

```bash
python nome_do_script.py
```

3. O script abrirá ambos os executáveis simultaneamente.

## Observações Finais

- Certifique-se de que os executáveis estejam no local correto antes de executar o script ou o binário compilado.
- Se estiver usando PyInstaller, inclua os executáveis no bundle usando o parâmetro `--add-data`.
- O script foi projetado para ser simples e eficiente, mas pode ser adaptado para outros executáveis ou cenários.
```
