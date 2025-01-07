document.addEventListener("DOMContentLoaded", () => {
  // Seleciona os elementos do DOM
  const checkButton = document.getElementById("check");
  const feedback = document.getElementById("feedback");
  const answerInput = document.getElementById("answer");
  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");
  const flashcardNumberElement = document.getElementById("flashcard-number");

  // Função para remover acentuação
  const removeAccents = (str) =>
    str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  // Função para remover pontuação
  const removePunctuation = (str) =>
    str.replace(/[.,!?;(){}[\]"/\\^%$#@&*+_=~`-]/g, "");

  // Função para normalizar a resposta (remove acentuação e pontuação)
  const normalizeString = (str) => removeAccents(removePunctuation(str)).toLowerCase();

  // Obtém a resposta correta do atributo "data-answer" do botão
  const correctAnswer = normalizeString(checkButton.dataset.answer);

  // Variável para contar o número de tentativas
  let attempts = 0;

  // Função para verificar a similaridade da resposta
  const getSimilarity = (userAnswer, correctAnswer) => {
    const userAnswerWords = userAnswer.split(" ");
    const correctAnswerWords = correctAnswer.split(" ");
    let commonWords = 0;

    userAnswerWords.forEach((word) => {
      if (correctAnswerWords.includes(word)) {
        commonWords++;
      }
    });

    // Retorna a porcentagem de palavras comuns entre as respostas
    return (commonWords / correctAnswerWords.length) * 100;
  };

  // Quando o botão for clicado, verifica a resposta
  checkButton.addEventListener("click", () => {
    const userAnswer = normalizeString(answerInput.value.trim());
    attempts++;

    if (userAnswer === correctAnswer) {
      feedback.textContent = `Correto! A resposta correta é: ${correctAnswer}.`;
      feedback.style.color = "green";
    } else {
      const similarity = getSimilarity(userAnswer, correctAnswer);

      if (attempts > 3) {
        // Se o usuário errou mais de 3 vezes, mostra a resposta correta
        feedback.textContent = `Você errou 3 vezes. A resposta correta é: ${correctAnswer}`;
        feedback.style.color = "red";
      } else {
        // Se o usuário ainda tem tentativas, mostra a similaridade
        feedback.textContent = `Tentativa ${attempts}. Você acertou ${similarity.toFixed(2)}% da resposta.`;
        feedback.style.color = "orange";
      }
    }
  });

  // Navegação entre páginas
  const currentPage = window.location.pathname.split("/").pop();
  const currentFlashcardNumber = currentPage.match(/\d+/);

  if (currentFlashcardNumber) {
    const flashcardNumber = currentFlashcardNumber[0];

    // Atualiza o número do flashcard na página
    flashcardNumberElement.textContent = flashcardNumber;

    // Atualiza o título da aba do navegador
    document.title = `Flashcard ${flashcardNumber}`;
  }

  // Navegação para a página anterior
  prevButton.addEventListener("click", () => {
    const currentNumber = parseInt(currentFlashcardNumber[0], 10);
    const prevPage = currentNumber === 1 ? 35 : currentNumber - 1;
    window.location.href = `card${prevPage}.html`;
  });

  // Navegação para a próxima página
  nextButton.addEventListener("click", () => {
    const currentNumber = parseInt(currentFlashcardNumber[0], 10);
    const nextPage = currentNumber === 35 ? 1 : currentNumber + 1;
    window.location.href = `card${nextPage}.html`;
  });
});
