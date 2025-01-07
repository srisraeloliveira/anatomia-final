import os

# Caminho da pasta com os arquivos
folder_path = r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\cara\cards"

# Nome base para os arquivos renomeados
base_name = "card"

# Obter a lista de arquivos na pasta
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Ordenar arquivos para manter a sequência (se necessário)
files.sort()

# Renomear arquivos sequencialmente
for index, filename in enumerate(files, start=1):
    # Caminho completo do arquivo antigo
    old_file = os.path.join(folder_path, filename)
    
    # Extensão do arquivo
    _, ext = os.path.splitext(filename)
    
    # Novo nome do arquivo
    new_file = os.path.join(folder_path, f"{base_name}{index}{ext}")
    
    # Renomear
    os.rename(old_file, new_file)
    print(f"Renomeado: {filename} -> {base_name}{index}{ext}")

print("Renomeação concluída!")
