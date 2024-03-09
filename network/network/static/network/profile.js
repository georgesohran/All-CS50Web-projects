document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#post-container-n').forEach((container) => {
        const num = container.dataset.num

        document.querySelector(`#edit-button-${num}`).onclick = () => {show_edit_field(num)}
        //get the edit button and make edit space
    })
})

function show_edit_field(num) {
    console.log(num)
    document.querySelector(`#post-body-${num}`).style.display = 'none'
    document.querySelector(`#edit-field-${num}`).style.display = 'block'
}

function cancel_edit_(num) {

}
