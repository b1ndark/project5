// sendMail function to send email using emailJS where I have set auto reply aswell. from Code Institute
function sendMail(contactForm) {
    // collects the values from the form
    emailjs.send('service_nxryx3l', 'template_30lav9g', {
        'from_name': contactForm.name.value,
        'from_subject': contactForm.subject.value,
        'from_email': contactForm.emailaddress.value,
        'from_message': contactForm.message.value
    });
}