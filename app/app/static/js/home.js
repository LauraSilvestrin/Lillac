function actionToggle() {
    var action = document.querySelector('.opcoes');
    var mais = document.querySelector('.mais');
    action.classList.toggle('active');
    mais.classList.toggle('active');
  }