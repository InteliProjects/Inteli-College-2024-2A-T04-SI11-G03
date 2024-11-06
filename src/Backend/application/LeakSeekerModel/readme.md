# Instalação do Ambiente

## 1.	Criação e Ativação do Ambiente Virtual (Opcional, mas Recomendado)
É recomendado criar um ambiente virtual para gerenciar as dependências do projeto. Para criar e ativar o ambiente virtual, use os seguintes comandos:

Windows
```bash
python -m venv .venv
```
```bash
.\.venv\Scripts\activate
```

macOS/Linux
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```

## 2. Instalação das Dependências

Após ativar o ambiente virtual, instale as bibliotecas necessárias usando o comando abaixo:

```bash
pip install -r requirements.txt
```