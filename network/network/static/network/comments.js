document.addEventListener('DOMContentLoaded' () => {
    document.querySelectorAll('#comment-button').forEach((button) => {
        button.onclick = make_comment
    })
})


function make_comment() {
    let cancel_buttons = document.querySelectorAll('#cancel-button')

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

