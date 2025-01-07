from bs4 import BeautifulSoup
import os

# Lista de caminhos de pastas onde os arquivos HTML estão localizados
folder_paths = [
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

# O código HTML a ser inserido
html_to_insert = """
<main>
  <h1 class="title-page">Flashcard <span id="flashcard-number">1</span></h1>
  <p class="question">Qual é a principal função do fígado?</p>
  <textarea id="answer" placeholder="Sua resposta"></textarea>
  <button id="check" data-answer="função de desintoxicação e produção de bile">Corrigir</button>
  <p class="feedback" id="feedback"></p>
</main>

<div id="navigation">
  <button id="prev">Anterior</button>
  <button id="next">Próximo</button>
</div>

<script src="../../../../js/script.js"></script>
"""

# Itera sobre cada pasta e arquivo HTML
for folder in folder_paths:
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            filepath = os.path.join(folder, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

                # Encontrar o header e inserir o HTML logo após ele
                header = soup.find('header')
                if header:
                    # Inserir o HTML após o <header>
                    header.insert_after(BeautifulSoup(html_to_insert, 'html.parser'))

                    # Salvar o arquivo modificado
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(str(soup))

            print(f"Conteúdo inserido no arquivo: {filepath}")