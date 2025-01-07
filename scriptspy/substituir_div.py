import os
import re

# Função para substituir a div em múltiplos diretórios
def substituir_div_em_arquivos(diretorios_base, div_antiga, div_nova):
    # Ajuste a div_antiga para ser uma string simples, sem indentação
    div_antiga_regex = re.escape(div_antiga.strip())  # Remove espaços extras e prepara para expressão regular
    div_nova = div_nova.strip()

    for diretorio_base in diretorios_base:
        print(f"Processando diretório: {diretorio_base}")
        # Percorre todos os arquivos dentro do diretório base e suas subpastas
        for root, dirs, files in os.walk(diretorio_base):
            for file in files:
                # Verifica se o arquivo é HTML
                if file.endswith(".html") or file.endswith(".htm"):  # Adapte conforme necessário
                    caminho_arquivo = os.path.join(root, file)
                    try:
                        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                            conteudo = f.read()

                        # Realiza a substituição da div, ignorando a indentação
                        # Usando a expressão regular para encontrar e substituir sem considerar a indentação
                        conteudo_modificado = re.sub(r'<div\s+id="navigation">\s*<button\s+id="prev">Anterior</button>\s*<button\s+id="next">Próximo</button>\s*</div>',
                                                     div_nova, conteudo)

                        # Se houver mudança, grava o novo conteúdo de volta no arquivo
                        if conteudo != conteudo_modificado:
                            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                                f.write(conteudo_modificado)
                            print(f"Alteração realizada em: {caminho_arquivo}")
                        else:
                            print(f"Div não encontrada no arquivo: {caminho_arquivo}")
                    except Exception as e:
                        print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")

# Defina os diretórios base onde estão os arquivos
diretorios_base = [
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

# Defina o conteúdo antigo e o novo conteúdo para substituir
div_antiga = '''<div id="navigation">
<button id="prev">Anterior</button>
<button id="next">Próximo</button>
</div>'''

div_nova = '''<div class="navigation" id="navigation">
<button id="prev">Anterior</button>
<button id="next">Próximo</button>
</div>'''

# Chama a função para realizar a substituição
substituir_div_em_arquivos(diretorios_base, div_antiga, div_nova)
