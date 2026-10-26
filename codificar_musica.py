from pathlib import Path

# Pasta onde está o código Python
pasta = Path(r"C:\Users\Guilherme Meins\Downloads")

# Arquivo original
arquivo_entrada = pasta / "musica.txt"

# Verifica se o arquivo existe
if not arquivo_entrada.exists():
    print("O arquivo musica.txt não foi encontrado.")
    print("Criando o arquivo musica.txt...")

    arquivo_entrada.touch()

    print(f"Arquivo criado em: {arquivo_entrada}")
    print("Abra o arquivo, insira a letra da música e salve.")
    print("Depois execute o programa novamente.")

else:
    # Leitura do arquivo original
    with open(arquivo_entrada, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    # Dicionário com as vogais e seus símbolos
    vogais = {
        "a": "!",
        "e": "@",
        "i": "#",
        "o": "$",
        "u": "%"
    }

    # Substituição das vogais
    texto_codificado = ""

    for letra in texto:
        if letra.lower() in vogais:
            texto_codificado += vogais[letra.lower()]
        else:
            texto_codificado += letra

    # Solicita o nome do arquivo de saída
    nome_arquivo = input(
        "Digite o nome do arquivo de saída (ex: resultado.txt): "
    ).strip()

    # Nome padrão caso o usuário não digite nada
    if not nome_arquivo:
        nome_arquivo = "resultado.txt"

    # Adiciona a extensão .txt caso necessário
    if not nome_arquivo.lower().endswith(".txt"):
        nome_arquivo += ".txt"

    # Caminho completo do arquivo de saída
    arquivo_saida = pasta / nome_arquivo

    # Evita sobrescrever o arquivo original
    if arquivo_saida.resolve() == arquivo_entrada.resolve():
        print("Erro: o arquivo de saída não pode ser musica.txt.")

    else:
        # Grava o texto codificado
        with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_codificado)

        print("\nConversão concluída com sucesso!")
        print("Arquivo criado:", arquivo_saida)