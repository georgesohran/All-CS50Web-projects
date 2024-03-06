document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        document.querySelector(`#cancel-button-${num}`).onclick = () => {cancel_comment(num)}
        document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}
    })
})

function show_comment_field(num) {
    document.querySelector(`#comment-text-${num}`).style.display = 'block'
    document.querySelector(`#cancel-button-${num}`).style.display = 'block'

    document.querySelector(`#comment-button-${num}`).onclick = () => {
    
    }
}

function cancel_comment(num) {
    document.querySelector(`#comment-text-${num}`).style.display = 'none'
    document.querySelector(`#cancel-button-${num}`).style.display = 'none'

    document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}
}
