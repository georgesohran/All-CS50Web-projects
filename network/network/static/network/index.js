document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-post-form').addEventListener('submit', () => {
        console.log('click')
        fetch('/api_make_post').then(response => response.json()).then((result) => {
            console.log(result)
        })
    })
})
