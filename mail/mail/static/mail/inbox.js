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
  document.querySelector('#email-details-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#submit-button').addEventListener('click', () => {
    fetch('emails/', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('compose-body').value,
      })
    .then(response => response.json())
    .then(result => {
      console.log(result);
      let msg_display = document.querySelector('#message')
        msg_display.innerHTML = result.message;
      })
    })
  })

  
}

function load_email(email_id) {
  console.log(email_id)

  document.querySelector('#email-details-view').style.display = 'block';
  document.querySelector('#email-details-view').innerHTML = '';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';

  fetch(`emails/${parseInt(email_id)}`).then(response => response.json()).then(email => {
    let email_content = document.createElement('div')
    email_content.innerHTML = `
        <p style="font-size:110%"><b>From:</b> ${email.sender}</p>
        <p style="font-size:110%"><b>To:</b>
          ${function() {
            ls = ''
            for(const reciver of email.recipients) {
              ls = ls + reciver + ','
            }
            return ls
          }()}
        </p>
        <p style="font-size:110%"><b>On timestamp:</b> ${email.timestamp}</p>
        <p style="font-size:110%"><b>Subject:</b> ${email.subject}</p>

        <p style="font-size:110%"><b>Contents:</b></p>
        <hr>
        <p style="font-size:120%">
          ${email.body}
        </p>
    `;
    document.querySelector('#email-details-view').append(email_content)
  })
}

function load_mailbox(mailbox) {

  console.log(mailbox)

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#emails-view').innerHTML = ''
  document.querySelector('#email-details-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h4>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h4b>`;

  fetch(`emails/${mailbox}`).then(response => response.json()).then(emails => {
    for(const email of emails) {
      let newEmail = document.createElement('div')
      newEmail.innerHTML = `
          <div class="email-list-element">
            <div class="email-info-cell"><button class="btn btn-sm btn-outline-primary" onclick="load_email(${email.id})"> See inside </button></div>
            <div class="email-info-cell" style="padding-top:2px">
              <b>${email.sender}</b>:&nbsp&nbsp
              <span style="font-size:110%">${email.subject}</span>
            </div>
            <div class="email-info-time">${email.timestamp}</div>
          </div>
      `;

      document.querySelector('#emails-view').append(newEmail)
    }
  })

}


