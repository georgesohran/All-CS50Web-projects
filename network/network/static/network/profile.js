document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#follow-button').onclick = follow

    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num

        document.querySelector(`#edit-button-${num}`).onclick = () => {show_edit_field(num)}
    })
})

function show_edit_field(num) {
    document.querySelector(`#post-body-${num}`).style.display = 'none'
    document.querySelector(`#edit-field-${num}`).style.display = 'block'

    document.querySelector(`#edit-text-${num}`).innerHTML = document.querySelector(`#main-post-contents-${num}`).innerHTML

    document.querySelector(`#save-edit-button-${num}`).onclick = () => {save_edit(num)}
    document.querySelector(`#cancel-edit-button-${num}`).onclick = () => {cancel_edit(num)}
}

function cancel_edit(num) {
    document.querySelector(`#post-body-${num}`).style.display = 'block'
    document.querySelector(`#edit-field-${num}`).style.display = 'none'
}

function save_edit(num) {
    new_contents = document.querySelector(`#edit-text-${num}`).value
    fetch(`/api_make_post`, {
        method:'PUT',
        body:JSON.stringify({new_contents:new_contents, post_id:num})
    }).then(response => response.json()).then((result) => {
        document.querySelector(`#post-body-${num}`).style.display = 'block'
        document.querySelector(`#edit-field-${num}`).style.display = 'none'
        document.querySelector(`#main-post-contents-${num}`).innerHTML = new_contents
        if('new_timestamp' in result) {
            document.querySelector(`#timestamp-${num}`).innerHTML = 'Edited - ' + result.new_timestamp
        }
    })
}

function follow() {
    
    fetch(`/api_follow/${}`, {method:'POST'}).then(response => response.json()).then((result) => {

    })
}
