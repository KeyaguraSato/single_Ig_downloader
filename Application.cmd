@echo off
:: Caminho do diretório onde está o script Python
cd /d "C:\Users\Miguel54658926\Desktop\insta downloader"

:: Verificar se a pasta 'downloads' existe, se não, criar
if not exist "downloads" (
    echo A pasta "downloads" nao existe. Criando...
    mkdir downloads
)

:: Ativar o ambiente virtual (verifica se o diretório venv existe)
if exist "venv\Scripts\activate" (
    call venv\Scripts\activate
    echo Ambiente virtual ativado.
) else (
    echo O ambiente virtual nao foi encontrado. Verifique o diretório 'venv'.
    exit /b
)

:: Executar o script Python
python main.py

:: Pausar para que a janela do terminal não feche imediatamente
pause
