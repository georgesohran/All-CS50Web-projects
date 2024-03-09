document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num

        document.querySelector(`edit-button-${num}`).onclick = () => {show_edit_field}
        //get the edit button and make edit space
    })
})

function show_edit_field(num) {

}

function cancel_edit_(num) {

}
