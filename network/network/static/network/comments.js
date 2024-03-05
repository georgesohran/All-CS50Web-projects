document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        let comment_button = document.querySelector(`[data-num]=${num}`)
        console.log(comment_button)
    })
})

