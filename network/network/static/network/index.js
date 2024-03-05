document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-post-form').addEventListener('submit', (event) => {
        event.preventDefault()
        fetch('/api_make_post', {
                method:"POST",
                body:JSON.stringify({contents : document.getElementById('contents').value})
        }).then(response => response.json()).then((result) => {
            document.getElementById('message').value = result.message
        })
    })
})
