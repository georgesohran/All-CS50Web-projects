document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}
    })
})

function show_comment_field(num) {
    document.querySelector(`#comment-button-${num}`)
}

function cancel_comment(num) {

}
