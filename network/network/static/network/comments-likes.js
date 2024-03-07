document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num
        document.querySelector(`#cancel-button-${num}`).onclick = () => {cancel_comment(num)}
        document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}

        document.querySelector(`#like-button-${num}`).onclick = () => {like(num)}

    })
})

function show_comment_field(num) {
    document.querySelector(`#comment-text-${num}`).style.display = 'block'
    document.querySelector(`#cancel-button-${num}`).style.display = 'block'

    document.querySelector(`#comment-button-${num}`).onclick = () => {
        fetch('/api_make_comment',{
            method:'POST',
            body:JSON.stringify({
                contents: document.querySelector(`#comment-text-${num}`).value,
                commented_post_id: num
            })
        }).then(response => response.json()).then((result) => {
            console.log(result)
            if('comment' in result) {
                comment = document.createElement('div')
                comment.className
            }
        })
    }
}

function cancel_comment(num) {
    document.querySelector(`#comment-text-${num}`).style.display = 'none'
    document.querySelector(`#cancel-button-${num}`).style.display = 'none'

    document.querySelector(`#comment-button-${num}`).onclick = () => {show_comment_field(num)}
}


function like(num) {
    fetch(`/api_like/${num}`, {method:'POST'}).then(response => response.json()).then((result) => {
        console.log(result)
        location.reload()
    })
}
