document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num

        document.querySelector(`#show-comments-${num}`).onclick = () => {show_comments(num)}

        document.querySelector(`#cancel-button-${num}`).onclick = () => {cancel_comment(num)}
        document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}

        document.querySelector(`#like-button-${num}`).onclick = () => {like(num)}
    })
})
