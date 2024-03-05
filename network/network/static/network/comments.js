document.addEventListener('DOMContentLoaded' () => {
    document.querySelectorAll('#post-container').forEach((container) => {
        let comment_button = container.getElementById('comment-button')
        comment_button.onclick = () => {
            let c_button = container.getElementById('cancel-button')
            let c_text = container.getElementById('comment-text')

            c_button.style.display = 'block'
            c_text.style.display = 'block'
            comment_button.onclick = make_comment

            container.getElementById('cancel-button').onclick = cancel_comment(comment_button)
        }
    })
})

function cancel_comment(btn, ) {

}

function make_comment() {

}
