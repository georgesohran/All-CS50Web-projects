document.addEventListener('DOMContentLoaded' () => {
    document.querySelectorAll('#post-container').forEach((container) => {
        let comment_button = container.getElementById('comment-button')
        comment_button.onclick = () => {
            container.getElementById('cancel-button').style.display = 'block'
            container.getElementById('comment-text').style.display = 'block'
            comment_button.onclick =
        }
    })
})

function make_comment() {
    
}
