document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').addEventListener('submit', (event) => {
    event.preventDefault()
    console.log(JSON.stringify({body: document.querySelector('#compose-body').value}))
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
      if(result.message){
        return load_mailbox('sent',{message: result.message, error: ''})
      } else if(result.error) {
        return compose_email({message: '', error: result.error})
      }
    })
  })
})

function archive_email(email_id, action) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({archived:action})
  }).then(() => {action ? load_mailbox('archive') : load_mailbox('inbox')})
}

function compose_email({message='', error='', recipients='', subject='', body=''}={}) {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-details-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#message').innerHTML = message;
  document.querySelector('#error').innerHTML = error;

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = recipients;
  document.querySelector('#compose-subject').value = subject;
  document.querySelector('#compose-body').value = body;
}

function load_email(email_id, sent) {
  console.log(email_id)
  document.querySelector('#email-details-view').style.display = 'block';
  document.querySelector('#email-details-view').innerHTML = '';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#message').innerHTML = '';
  document.querySelector('#error').innerHTML = '';

  let email

  fetch(`emails/${email_id}`).then(response => response.json()).then(email => {
    let email_content = document.createElement('div')
    console.log(email.body)
    email_content.innerHTML = `
        <p style="font-size:110%"><b>From:</b> ${email.sender}</p>
        <p style="font-size:110%"><b>To:</b>
          ${
            function() {
              ls = ''
              for(const reciver of email.recipients) {
                ls = ls + reciver + ','
              }
              return ls
            }()
          }
        </p>
        <p style="font-size:110%"><b>On timestamp:</b> ${email.timestamp}</p>
        <p style="font-size:110%"><b>Subject:</b> ${email.subject}</p>

        <p style="font-size:110%"><b>Contents:</b></p>
        <hr>
        <div style="font-size:120%; white-space: pre-line">
          ${email.body}
        </div>
        <br>
    `;
    document.querySelector('#email-details-view').append(email_content)

    if(!sent){
      let archive_button = document.createElement('button')
      archive_button.className = 'btn btn-primary'
      archive_button.innerHTML = email.archived ? 'Unarchive this email' : 'Archive this email'
      archive_button.addEventListener('click', () => archive_email(email_id, !email.archived))
      document.querySelector('#email-details-view').append(archive_button)

      let reply_button = document.createElement('button')
      reply_button.className = 'btn btn-primary'
      reply_button.innerHTML = 'Reply to this email'
      reply_button.addEventListener('click', () => {
        compose_email({message:'Replying to an email', error:'',
          recipients: email.recipients,
          subject: email.subject.includes('Re')? 'Re:'+email.subject : email.subject,
          body: `On ${email.timestamp}: ${email.sender} wrote:\n${email.body}`})
      })
      document.querySelector('#email-details-view').append(reply_button)
    }

    if(!email.read) {
      return fetch(`emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({read:true})
      })
    }
  });
}

function load_mailbox(mailbox, {message = '', error = ''}={}) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#emails-view').innerHTML = ''
  document.querySelector('#email-details-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#message').innerHTML = message;
  document.querySelector('#error').innerHTML = error;

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h4>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h4b>`;

  fetch(`emails/${mailbox}`).then(response => response.json()).then(emails => {
    for(const email of emails) {
      let newEmail = document.createElement('div')
      if(mailbox == 'sent') {
        newEmail.innerHTML = `
        <div class="email-list-element">
          <div class="email-info-cell">
            <button class="btn btn-sm btn-outline-primary" onclick="load_email(${email.id}, true)"> See inside </button>
          </div>
          <div class="email-info-cell" style="padding-top:2px">
            <b>${email.sender}</b>:&nbsp&nbsp
            <span style="font-size:110%">${email.subject}</span>
          </div>
          <div class="email-info-time">${email.timestamp}</div>
        </div>
        `;
      } else {
        newEmail.innerHTML = `
        <div class="email-list-element" ${email.read ? 'style="color:gray;border-color:gray"':''}>
          <div class="email-info-cell">
            <button class="btn btn-sm btn-outline-primary" onclick="load_email(${email.id}, false)"> See inside </button>
            <button class="btn btn-sm btn-outline-primary" onclick="archive_email(${email.id},${!email.archived})"> ${email.archived ? 'Unarchive' : 'Archive'}</button>
          </div>
          <div class="email-info-cell" style="padding-top:2px">
            <b>${email.sender}</b>:&nbsp&nbsp
            <span style="font-size:110%">${email.subject}</span>
            ${email.read ? '&nbsp&nbsp&nbsp<span style="font-size:110%">READ</span>':''}
          </div>
          <div class="email-info-time">${email.timestamp}</div>
        </div>
        `;
      }
      document.querySelector('#emails-view').append(newEmail)
    }
  })
};
