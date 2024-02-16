document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  console.log(mailbox)

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#emails-view').innerHTML = ''
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  let heading

  document.querySelector('#emails-view').innerHTML = `<h4>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h4b>`;

  fetch(`emails/${mailbox}`).then(response => response.json()).then(emails => {
    for(const email of emails) {
      let newEmail = document.createElement('div')
      newEmail.setAttribute('class', 'email-list-element')
      newEmail.innerHTML = `
        <span>
          <b>${email.sender}</b>
          <p>${email.timestamp}</p>
        </span>
      `;

      document.querySelector('#emails-view').append(newEmail)
    }
  })

}

function load_email(email) {
//TODO
}
