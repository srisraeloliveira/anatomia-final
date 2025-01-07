import os

# Caminho da pasta principal
root_folder = r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final"

# Código do footer a ser inserido
footer_content = """
<footer>
    <p>&copy; 2025 Estudos de Anatomia</p>
</footer>
"""

# Percorrer a pasta principal e todas as subpastas
for folder_path, subfolders, files in os.walk(root_folder):
    # Processar apenas arquivos HTML
    html_files = [f for f in files if f.endswith('.html')]
    
    for html_file in html_files:
        file_path = os.path.join(folder_path, html_file)
        
        # Ler o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verificar se o footer já está presente
        if footer_content.strip() in content:
            print(f"Footer já presente em: {file_path}")
            continue
        
        # Inserir o footer antes da tag </body>
        if "</body>" in content:
            content = content.replace("</body>", f"{footer_content}\n</body>")
        else:
            # Caso o arquivo não tenha </body>, adiciona no final
            content += f"\n{footer_content}"
        
        # Escrever o conteúdo de volta ao arquivo
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Footer adicionado em: {file_path}")

print("Processo concluído!")
