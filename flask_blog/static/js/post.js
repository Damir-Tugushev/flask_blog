function handle_post(url, post_id, no_posts) {
    const object = {id: post_id};
    post_json(url, object)
        .then(response => {
            if (!response.ok) return Promise.reject(response);
            return response.json();
        })
        .then(data => {
            console.log(data);
            const post = document.getElementById(post_id);
            post.remove();

            const post_list = document.getElementById('post_list');
            if (post_list.children.length === 0) {
                const div = document.createElement('div');
                div.innerHTML = no_posts.trim();
                const replacement = div.firstChild;
                post_list.parentNode.replaceChild(replacement, post_list);
            }
        })
        .catch(error => error.json().then(error => console.warn(error)));
}
