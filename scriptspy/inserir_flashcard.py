import os
from bs4 import BeautifulSoup

# Caminhos dos diretórios onde estão os arquivos HTML
diretorios = [
   r"C:\Users\israd\OneDrive\Área de Trabalho\anatomia final\esplacnologia\submodulos\abdomeninfraretro\cards"
]

# Exemplo de perguntas e respostas

flashcards = {
    1: {"pergunta": "¿Cuál es la principal irrigación del abdomen inframesocólico?", "resposta": "Mesentérica superior e inferior."},
    2: {"pergunta": "¿Qué plexo es responsable de la mayor parte de la inervación del abdomen inframesocólico?", "resposta": "Plexo mesentérico superior."},
    3: {"pergunta": "¿Dónde termina la linfa del abdomen inframesocólico?", "resposta": "En los nodos mesentéricos superiores e inferiores."},
    4: {"pergunta": "¿Cuál es el límite superior del abdomen inframesocólico?", "resposta": "Mesocolon transverso."},
    5: {"pergunta": "¿Qué vísceras del abdomen inframesocólico están peritonealizadas?", "resposta": "Todas las vísceras."},
    6: {"pergunta": "¿Qué divide el abdomen inframesocólico en dos regiones?", "resposta": "El mesenterio."},
    7: {"pergunta": "¿Qué vísceras están en el mesenterio superior?", "resposta": "Yeyuno-íleon, apéndice, ciego, colon ascendente, flexura cólica derecha y dos tercios proximales del colon transverso."},
    8: {"pergunta": "¿Qué vísceras están en el mesenterio inferior?", "resposta": "Menos yeyuno-íleon, el tercio distal del colon transverso, colon descendente, sigmoide y porción superior del recto."},
    9: {"pergunta": "¿Dónde se encuentra el yeyuno-íleon?", "resposta": "Entre L1 y L5-S1, en el mesogastrio."},
    10: {"pergunta": "¿Cuál es la principal función del yeyuno-íleon?", "resposta": "Absorción de nutrientes."},
    11: {"pergunta": "¿Dónde se encuentra el apéndice vermiforme?", "resposta": "Inferomedial al ciego, en la zona inguinal derecha."},
    12: {"pergunta": "¿Cuál es la irrigación del apéndice vermiforme?", "resposta": "Arteria apendicular, que sale del tronco ileocólico."},
    13: {"pergunta": "¿Cuál es la principal función del ciego?", "resposta": "Almacenamiento y absorción de líquidos del contenido intestinal."},
    14: {"pergunta": "¿Dónde se localiza el colon ascendente?", "resposta": "En el flanco derecho."},
    15: {"pergunta": "¿Cuál es la principal función del colon ascendente?", "resposta": "Absorción de agua de la materia fecal."},
    16: {"pergunta": "¿Dónde se localiza la flexura cólica derecha (hepática)?", "resposta": "A nivel de L1/L2, en el hipocondrio derecho."},
    17: {"pergunta": "¿Cuál es la principal función del colon transverso?", "resposta": "Absorción de agua de la materia fecal."},
    18: {"pergunta": "¿Dónde se encuentra el colon descendente?", "resposta": "En el flanco izquierdo."},
    19: {"pergunta": "¿Cuál es la principal función del colon descendente?", "resposta": "Almacenamiento y conducción de materia fecal."},
    20: {"pergunta": "¿Dónde se encuentra el retroperitoneo?", "resposta": "Posterior a la hoja posterior del peritoneo parietal."},
    21: {"pergunta": "El abdomen inframesocólico es irrigado principalmente por las arterias ________ y ________.", "resposta": "mesentérica superior e inferior."},
    22: {"pergunta": "La principal inervación del abdomen inframesocólico proviene del plexo ________.", "resposta": "mesentérico superior."},
    23: {"pergunta": "El mesenterio divide el abdomen inframesocólico en dos regiones: ________ y ________.", "resposta": "mesenterio superior y mesenterio inferior."},
    24: {"pergunta": "El apéndice vermiforme está irrigado por la arteria ________.", "resposta": "apendicular."},
    25: {"pergunta": "El ciego es una porción del intestino grueso y está localizado en la región ________.", "resposta": "inguinal derecha."},
    26: {"pergunta": "El colon ascendente está localizado en el ________.", "resposta": "flanco derecho."},
    27: {"pergunta": "El colon transverso está localizado en el ________.", "resposta": "mesogastrio."},
    28: {"pergunta": "La irrigación del colon ascendente proviene de la arteria ________.", "resposta": "cólica derecha."},
    29: {"pergunta": "La flexura cólica derecha se localiza a nivel de ________.", "resposta": "L1/L2."},
    30: {"pergunta": "El colon descendente está fijado por la fascia ________.", "resposta": "retrocolica izquierda."},
    31: {"pergunta": "El apéndice vermiforme está fijado por un meso llamado ________.", "resposta": "meso apéndice."},
    32: {"pergunta": "El colon sigmoide está localizado en la región ________.", "resposta": "inguinal derecha."},
    33: {"pergunta": "El retroperitoneo está limitado anteriormente por la ________.", "resposta": "hoja posterior del peritoneo parietal."},
    34: {"pergunta": "El retroperitoneo está limitado inferiormente por el ________.", "resposta": "promontorio."},
    35: {"pergunta": "El mesenterio del colon transverso se llama ________.", "resposta": "mesocolon transverso."},
}


# Função para inserir as perguntas e respostas no arquivo
def inserir_flashcard_no_arquivo(caminho_arquivo, numero_flashcard):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    soup = BeautifulSoup(conteudo, 'html.parser')

    # Encontrar o elemento <span id="flashcard-number"> e atualizar o número
    flashcard_number = soup.find('span', {'id': 'flashcard-number'})
    if flashcard_number:
        flashcard_number.string = str(numero_flashcard)

    # Encontrar o elemento <p class="question"> e atualizar a pergunta
    question_tag = soup.find('p', {'class': 'question'})
    if question_tag:
        question_tag.string = flashcards[numero_flashcard]['pergunta']

    # Encontrar o elemento <button id="check"> e atualizar a resposta
    check_button = soup.find('button', {'id': 'check'})
    if check_button:
        check_button['data-answer'] = flashcards[numero_flashcard]['resposta']

    # Reescreve o conteúdo do arquivo com as alterações
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Percorre os diretórios e arquivos para inserir as perguntas e respostas
for diretorio in diretorios:
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(".html"):  # Certifique-se de que o arquivo é HTML
                caminho_arquivo = os.path.join(root, file)
                
                # Extrair o número do flashcard do nome do arquivo (cardX.html)
                if file.startswith('card') and file.endswith('.html'):
                    numero_flashcard = int(file.replace('card', '').replace('.html', ''))

                    # Se o número do flashcard estiver no dicionário de flashcards, insira a pergunta e resposta
                    if numero_flashcard in flashcards:
                        inserir_flashcard_no_arquivo(caminho_arquivo, numero_flashcard)
                        print(f"Flashcard {numero_flashcard} atualizado em: {caminho_arquivo}")
