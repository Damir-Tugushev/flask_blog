function handle_submit_form_error(error) {
    error.json().then(error => {
        console.warn(error);

        const fields = form.querySelectorAll('.form-control');
        fields.forEach(field => field.className = 'form-control is-valid');

        for (const id in error.errors) {
            const text = error.errors[id].join('\n');
            const field = document.getElementById(id);
            field.className = 'form-control is-invalid';

            const feedback = field.parentElement.querySelector('div.invalid-feedback');
            feedback.innerText = text;
        }
    })
}

function submit_auth_form(login_form_url, csrf_token, form) {
    const form_data = new FormData(form);
    post_form(login_form_url, form_data, csrf_token)
        .then(response => {
            if (!response.ok) return Promise.reject(response);
            return response.json();
        })
        .then(data => {
            const fields = form.querySelectorAll('.form-control');
            fields.forEach(field => field.className = 'form-control is-valid');
            window.location.replace(data.url);
        })
        .catch(handle_submit_form_error);
}

function submit_create_post_form(url, get_post_url, get_user_url, user_url, csrf_token, form) {
    const form_data = new FormData(form);
    post_form(url, form_data, csrf_token)
        .then(response => {
            if (!response.ok) return Promise.reject(response);
            return response.json();
        })
        .then(data => {
            const fields = form.querySelectorAll('.form-control');
            fields.forEach(field => field.className = 'form-control is-valid');

            const post_id = data.id;
            const url = get_post_url.replace(REPLACE, post_id);
            fetch(url).then(response => response.json()).then(post => {
                const title = post.title;
                const text_content = post['text_content'];
                const author_id = post['author_id'];
                const url = get_user_url.replace(REPLACE, author_id);
                fetch(url).then(response => response.json()).then(user => {
                    const login = user['login'];
                    const post_list = document.getElementById('post_list');

                    const div = document.createElement('div');
                    const _user_url = user_url.replace(REPLACE, login);
                    div.innerHTML = `
                        <li class="list-group-item d-flex justify-content-between align-items-start"
                            id="${post_id}">
                            <div class="ms-2 m-1 w-100">
                                <h5 class="d-inline-block w-100" style="overflow-wrap: break-word;">
                                    <a class="fw-bold" href="${_user_url}">${login}</a>: ${title}
                                </h5>
                                <span class="d-inline-block w-100" style="overflow-wrap: break-word">
                                    ${text_content}
                                </span>
                            </div>
                        </li>
                    `.trim();
                    const post = div.firstChild;
                    const first_post = post_list.querySelector('li');
                    post_list.insertBefore(post, first_post);
                });
            });
        })
        .catch(handle_submit_form_error);
}
