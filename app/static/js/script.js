document.addEventListener('DOMContentLoaded', function () {
  const quantidadeEl = document.getElementById('quantidade');
  const precoEl = document.getElementById('preco_unitario');
  const descontoEl = document.getElementById('desconto');

  const valorSemDescontoDisplay = document.getElementById('valor_sem_desconto');
  const valorFinalDisplay = document.getElementById('valor_final');

  const valorSemDescontoInput = document.getElementById('valor_sem_desconto_input');
  const valorFinalInput = document.getElementById('valor_final_input');

  function parseNumber(v) {
    const n = parseFloat(String(v).replace(',', '.'));
    return isNaN(n) ? 0 : n;
  }

  function formatBRL(n) {
    return n.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function calcular() {
    const quantidade = Math.max(0, parseInt(quantidadeEl.value || 0, 10));
    const preco = Math.max(0, parseNumber(precoEl.value));
    const desconto = Math.max(0, parseNumber(descontoEl.value));

    const valorSem = +(preco * quantidade);
    let valorFinal = valorSem - desconto;
    if (valorFinal < 0) valorFinal = 0;

    valorSemDescontoDisplay.textContent = 'R$ ' + formatBRL(valorSem);
    valorFinalDisplay.textContent = 'R$ ' + formatBRL(valorFinal);

    // popula inputs para envio (com ponto decimal)
    valorSemDescontoInput.value = valorSem.toFixed(2);
    valorFinalInput.value = valorFinal.toFixed(2);
  }

  quantidadeEl.addEventListener('input', calcular);
  precoEl.addEventListener('input', calcular);
  descontoEl.addEventListener('input', calcular);

  // calcular na carga
  calcular();
});
