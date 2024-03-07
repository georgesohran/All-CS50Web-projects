document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-post-form').addEventListener('submit', (event) => {
        event.preventDefault()
        fetch('/api_make_post', {
                method:"POST",
                body:JSON.stringify({contents : document.getElementById('contents').value})
        }).then(response => response.json()).then((result) => {
            document.getElementById('message').innerHTML = result.message
        })
    })

    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
    })
})
