document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('riskScore').textContent = data.risk_score;
        document.getElementById('country').textContent = data.country;
        document.getElementById('carrier').textContent = data.carrier;
        document.getElementById('validity').textContent = data.validity;
        document.getElementById('fraudulent').textContent = data.fraudulent ? 'Yes' : 'No';
        document.getElementById('result').classList.remove('hidden');
    })
    .catch(error => console.error('Error:', error));
});
