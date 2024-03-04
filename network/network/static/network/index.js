document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('nem-post-form').addEventListener('submit', () => {
        fetch("/api_make_post").then(response => response.json()).then((result) => {
            console.log(result)
        })
    })
})
