document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num

        document.querySelector(`#show-comments-${num}`).onclick = () => {show_comments(num)}

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
                comment.className = 'comment-container'
                comment.innerHTML =  `
                    <p><b>${result.comment.creator}</b> --- <span style="color:gray">${result.comment.timestamp}</span><p>
                    <p>${result.comment.body}</p>
                `
                let comment_txt = document.querySelector(`#comment-text-${num}`)
                document.querySelector(`#comments-${num}`).insertBefore(comment, comment_txt)
                cancel_comment(num)
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
        like_element = document.querySelector(`#like-button-${num}`)
        like_element.className = result.user_like ? 'badge badge-primary' : 'badge badge-light'
        like_element.innerHTML = `❤️ ${result.likes}`
    })
}


function show_comments(num) {
    document.querySelector(`#comments-${num}`).style.display = 'block'

    document.querySelector(`#show-comments-${num}`).innerHTML = 'Hide comments'
    document.querySelector(`#show-comments-${num}`).onclick = () => {hide_comments(num)}
}
function hide_comments(num) {
    document.querySelector(`#comments-${num}`).style.display = 'none'

    document.querySelector(`#show-comments-${num}`).innerHTML = 'Show comments'
    document.querySelector(`#show-comments-${num}`).onclick = () => {show_comments(num)}
}
