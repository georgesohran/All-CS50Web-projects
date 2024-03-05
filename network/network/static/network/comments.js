document.addEventListener('DOMContentLoaded' () => {
    document.querySelectorAll('#comment-button').forEach((button) => {
        button.onclick = make_comment
    })
})


function make_comment() {
    document.querySelectorAll('#cancel-button').forEach((button) => {
        button.style.display = 'block'
        button.onclick = () => {
            button.style.display = 'none'
        }
    })

    document.querySelectorAll('#comment-text').forEach((textarea) => {
        textarea.style.display = 'block'
        document.querySelectorAll('#comment-button').forEach((button) => {
            button.onclick = () => {
                //fetch stuff to the server
            }
        })
    })
}


function like() {

}

