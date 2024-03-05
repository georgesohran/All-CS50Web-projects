document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        let comment_button = document.querySelector(`#comment-button-${num}`)
        let cancel_button = document.querySelector(`#cancel-button-${num}`)
        let comment_text = document.querySelector(`#comment-text-${num}`)

        console.log(comment_button)
    })
})

