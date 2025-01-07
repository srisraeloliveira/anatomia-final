import os
from bs4 import BeautifulSoup

# Caminhos dos diretórios
diretorios = [
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\abdomen1\cards",  # Substitua pelo primeiro caminho
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\abdomeninfraretro\cards",  # Substitua pelo segundo caminho
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\abdomensupramesolico\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\cara\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\cuello\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\mediastino\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\pelvis\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\pelvisperine\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\torax\cards",  # Substitua pelo terceiro caminho, etc.
    r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\vago\cards"  # Substitua pelo terceiro caminho, etc.
]

# Função para remover a tag <script> específica de um arquivo
def remover_script_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    soup = BeautifulSoup(conteudo, 'html.parser')

    # Remove a tag <script> com o src específico
    script_tag = soup.find('script', {'src': '../../../../js/script.js'})
    if script_tag:
        script_tag.decompose()

    # Reescreve o conteúdo do arquivo com as alterações
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Percorre os diretórios e arquivos para remover a tag <script>
for diretorio in diretorios:
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(".html"):  # Certifique-se de que o arquivo é HTML
                caminho_arquivo = os.path.join(root, file)
                remover_script_do_arquivo(caminho_arquivo)
                print(f"Tag <script> removida do arquivo: {caminho_arquivo}")
