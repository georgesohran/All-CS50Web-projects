document.addEventListener('DOMContentLoaded' () => {
    document.querySelectorAll('#post-container').forEach((container) => {
        let comment_button = container.getElementById('comment-button')
        comment_button.onclick = () => {
            let c_button = container.getElementById('cancel-button')
            let c_text = container.getElementById('comment-text')

            c_button.style.display = 'block'
            c_text.style.display = 'block'
            comment_button.onclick = make_comment

            c_button.onclick = () => {cancel_comment(c_button, c_text); }
        }
    })
})

function cancel_comment(btn, txt) {
    btn.style.display = 'none'
    txt.style.display = 'none'
}

function make_comment() {

}
