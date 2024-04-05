document.body.addEventListener('htmx:afterRequest', function(event) {
    if (event.detail.path === '/ping' || event.detail.path === '/echo') {
        document.getElementById('echo-data').value = '';
    }
});

document.body.addEventListener('htmx:afterOnLoad', function(event) {
    let response = event.detail.xhr.response;
    try {
        let jsonResponse = JSON.parse(response);
        if (event.detail.path === '/ping') {
            updateStatus(jsonResponse.message, 'success');
        } else if (event.detail.path === '/echo') {
            updateStatus(jsonResponse.resposta, 'success');
        }
    } catch (e) {
        updateStatus('Error processing the response.', 'error');
    }
});