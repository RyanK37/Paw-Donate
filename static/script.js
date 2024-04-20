document.addEventListener('DOMContentLoaded', function() {
    var donateButtons = document.querySelector('.donatebuttons');
    var amountInput = document.getElementById('amount');

    donateButtons.addEventListener('click', function(event) {
        if (event.target.tagName === 'IMG') {
            var amount = event.target.getAttribute('data-amount');
            amountInput.value = amount;
        }
    });
});