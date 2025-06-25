document.getElementById('animalForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const animalInput = document.getElementById('animalInput').value;
    const resultArea = document.getElementById('resultArea');
    const loadingSpinner = document.getElementById('loadingSpinner');

    resultArea.innerHTML = '';
    loadingSpinner.style.display = 'block';

    try {
        const res = await fetch('/search', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ animal_name: animalInput })
        });

        const data = await res.json();
        loadingSpinner.style.display = 'none';

        if (data.error) {
            resultArea.innerHTML = `
                <div class="alert alert-warning fade-in" role="alert">
                    No information found for <strong>${animalInput}</strong>.
                </div>`;
        } else {
            let list = '<ul class="list-group fade-in">';
            for (const [key, value] of Object.entries(data)) {
                list += `
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <strong>${key}</strong>
                        <span>${value}</span>
                    </li>`;
            }
            list += '</ul>';
            resultArea.innerHTML = `
                <h5 class="result-title fade-in">Details for <strong>${animalInput}</strong>:</h5>
                ${list}`;
        }
    } catch (error) {
        loadingSpinner.style.display = 'none';
        resultArea.innerHTML = `
            <div class="alert alert-danger fade-in" role="alert">
                An error occurred. Please try again later.
            </div>`;
    }
});
