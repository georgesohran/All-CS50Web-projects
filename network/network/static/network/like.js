//implement likes here

function like() {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        document.querySelector(`#cancel-button-${num}`).onclick = () => {cancel_comment(num)}
        document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}
    })
}

function unlike() {

}
