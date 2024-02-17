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

function load_email(email_id) {
  console.log(email_id)

  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#email-view').innerHTML = '';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';

  fetch(`emails/${email_id}`).then(response => response.json()).then(email => {
    let test = document.createElement('p')
    test.innerHTML = 'Hello, this is test mail'
    document.querySelector('#email-view').append(test)
  })

}

function load_mailbox(mailbox) {

  console.log(mailbox)

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#emails-view').innerHTML = ''
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h4>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h4b>`;

  fetch(`emails/${mailbox}`).then(response => response.json()).then(emails => {
    for(const email of emails) {
      let newEmail = document.createElement('div')
      newEmail.innerHTML = `
        <div class="email-list-element">
          <div class="email-info-cell"><button class="btn btn-primary" onclick="load_email(${email.id})"> See inside </button></div>
          <div class="email-info-cell"><b>${email.sender}</b></div>
          <div class="email-info-cell"><span style="font-size:110%">${email.subject}</span></div>
          <div class="email-info-time">${email.timestamp}</div>
        </div>
      `;

      document.querySelector('#emails-view').append(newEmail)
    }
  })

}


