const alertSec = document.getElementById("alert-section")
const message = document.getElementById("alert-message");

function sendEmail(name, surname, email, message) {
    emailjs.send("Gmail", "template_gk9xrex", {
            "from_name": name.value,
            "from_surname": surname.value,
            "from_email": email.value,
            "request": message.value,
        })
        .then(
            function (response) {
                let form = document.getElementById("contactForm");
                form.innerHTML = "<h2>Vielen Dank für Ihre Nachricht! Wir werden Ihnen sobald wie möglich ein Antwort schicken!</h2>"
                console.log("success", response)
            },
            function (error) {
                let form = document.getElementById("contactForm");
                form.innerHTML = "<h2>Error: Es gab einen Fehler bei der Zusendung der Nachricht. Bitte versuchen Sie es später nochmal!</h2>"
                console.log("fail", error)
            }
        );
    // Block from loading a new page
    return false;
}

const submit = document.getElementById("submitBtn");
let nameInput = document.getElementById("name");
let surnameInput = document.getElementById("surname");
let emailInput = document.getElementById("email");
let messageInput = document.getElementById("contactMessage");

submit.addEventListener("click", function (event) {
    // This prevents the default action of the form and then calls the sendMsg function
    event.preventDefault();
    sendMsg();
});

function sendMsg() {
    let nameContent = nameInput.value.trim();
    let surnameContent = surnameInput.value.trim();
    let emailContent = emailInput.value.trim();
    let msgContent = messageInput.value.trim();
    let mailValidation = /^[a-zA-Z0-9._-]+@[a-zA-z0-9.-]+\.[a-zA-Z-0-9]{2,4}$/

    // Alerts pop up, if a required field has not been filled in, before pressing on the submit
    if(nameContent == '' || surnameContent == '' || emailContent == '' || msgContent == '') {
        alertSec.className = "alert alert-danger";
        alertSec.innerHTML = "<h4>Bitte füllen Sie alle Felder aus.</h4>"
    }
    else {
        if (nameContent.length < 2) {
            alertSec.className = "alert alert-danger";
            alertSec.innerHTML = "<h4>Ihr Name muss mindestens zwei Charaktere erhalten.</h4>"
        } else if (surnameContent.length < 2) {
            alertSec.className = "alert alert-danger";
            alertSec.innerHTML = "<h4>Ihr Nachname muss mindestens zwei Charaktere erhalten.</h4>"
        } else if (!emailContent.match(mailValidation)) {
            alertSec.className = "alert alert-danger";
            alertSec.innerHTML = "<h4>Bitte geben Sie eine gültige E-Mail Adresse ein.</h4>"
        } else if (msgContent.length < 10) {
            alertSec.className = "alert alert-danger";
            alertSec.innerHTML = "<h4>Ihre Nachricht muss mindestens 10 Charaktere erhalten.</h4>"
        }
        // The sendMail function gets called, if each of the required fields on the page have been filled in
        else {
            sendEmail(nameInput, surnameInput, emailInput, messageInput);
        }
    }
}