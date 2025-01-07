import os
import re

# Caminho da pasta principal
root_folder = r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final"

# Padrão do footer (com regex para ignorar espaços e quebras de linha)
footer_pattern = re.compile(r"""
<footer>\s*                # Tag <footer> com possíveis espaços
<p>\s*&copy;\s*2025\s+Estudos\s+de\s+Anatomia\s*</p>\s*  # Conteúdo do parágrafo
</footer>                 # Fechamento da tag <footer>
""", re.VERBOSE)

# Contador de footers removidos
removed_count = 0

# Percorrer a pasta principal e todas as subpastas
for folder_path, subfolders, files in os.walk(root_folder):
    # Processar apenas arquivos HTML
    html_files = [f for f in files if f.endswith('.html')]
    
    for html_file in html_files:
        file_path = os.path.join(folder_path, html_file)
        
        # Ler o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Encontrar todas as ocorrências do footer
        matches = footer_pattern.findall(content)
        
        if len(matches) > 1:
            # Remove todas as ocorrências do footer
            content = footer_pattern.sub("", content)
            
            # Adiciona apenas uma ocorrência ao final do arquivo
            content = content.strip() + "\n\n<footer>\n    <p>&copy; 2025 Estudos de Anatomia</p>\n</footer>\n"
            
            # Atualiza o contador de footers removidos
            removed_count += len(matches) - 1
            
            # Escrever o conteúdo atualizado de volta ao arquivo
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Footers duplicados removidos em: {file_path}")

# Exibir o total de footers removidos
print(f"\nTotal de footers duplicados removidos: {removed_count}")
