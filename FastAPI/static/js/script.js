document.getElementById('action-btn').addEventListener('click', () => {
    const resultParagraph = document.getElementById('result');
    resultParagraph.textContent = 'Привет из JavaScript! Фронтенд успешно работает.';
    resultParagraph.style.color = '#28a745';
});