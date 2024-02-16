function calculate() {
    var num1 = document.getElementById('num1').value.trim();
    var operation = document.getElementById('operation').value;
    var num2 = document.getElementById('num2').value.trim();

    if (!num1 || !num2) {
        alert('Please enter binary numbers');
        return;
    }

    fetch('/binmath', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num1: num1,
            num2: num2,
            operation: operation
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Result: ' + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}