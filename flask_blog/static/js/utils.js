const REPLACE = 'REPLACE';

function post_json(url, json) {
    const init = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(json),
    };
    return fetch(url, init);
}

function post_form(url, form, csrf_token) {
    if (!(form instanceof FormData)) throw Error('form must be instance of FormData class');
    const init = {
        method: 'POST',
        headers: {'X-CSRFToken': csrf_token},
        body: form,
    };
    return fetch(url, init);
}
