document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-post-form').addEventListener('submit', (event) => {
        event.preventDefault()
        console.log('click')
        fetch('/api_make_post', {
                method:"POST",
                body:JSON.stringify({contents : document.getElementById('contents').value})
        }).then(response => response.json()).then((result) => {
            console.log(result)
        })
    })
})
