const scoreele = document.getElementById('score');;

document.getElementById('send').addEventListener('click', function() {
  const score = scoreele.textContent;
  const scoreForm = document.getElementById('score_form');
  const scoreInput = document.getElementById('score_input');
  scoreInput.value = score;
  scoreForm.submit();
});