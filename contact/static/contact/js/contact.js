function sendEmail(name, surname, email, message) {
    emailjs.send("Gmail", "template_gk9xrex", {
            "from_name": name,
            "from_surname": surname,
            "from_email": email,
            "request": message,
        })
        .then(
            function (response) {
                let form = document.getElementById("contactForm");
                form.innerHTML = "<h2>Vielen Dank für Ihre Nachricht! Wir werden Ihnen sobald wie möglich ein Antwort schicken!"
                console.log("success", response)
            },
            function (error) {
                let form = document.getElementById("contactForm");
                form.innerHTML = "<h2>Error: Es gab einen Fehle bei der Zusendung der Nachricht. Bitte versuchen Sie es später nochmal!"
                console.log("fail", error)
            }
        );
        // Block from loading a new page
        return false;
}
window.onload = function() {
    const submit = document.getElementById("submitBtn");
    const nameInput = document.getElementById("name");
    const surnameInput = document.getElementById("surname");
    const emailInput = document.getElementById("email");
    const messageInput = document.getElementById("contactMessage");

    submit.addEventListener("click", function(event)
    {
        // This prevents the default action of the form and then calls the sendMsg function
        event.preventDefault();
        sendMsg();
    });

    function sendMsg() {
        let emailContent = emailInput.value;
        let MsgContent = messageInput.value;
        let mailValidation = /^[a-zA-Z0-9._-]+@[a-zA-z0-9.-]+\.[a-zA-Z-0-9]{2,4}$/

        // Alerts pop up, if a required field has not been filled in, before pressing on the submit
        if (!emailContent.match(mailValidation)) {
            alert('Bitte geben Sie eine gültige E-Mail Adresse ein');
        }
        else if (MsgContent === '') {
            alert('');
        }
        // The sendMail function gets called, if each of the required fields on the page have been filled in
        else {
            sendEmail(nameInput, surnameInput, emailInput, messageInput)
        }
    }
}

