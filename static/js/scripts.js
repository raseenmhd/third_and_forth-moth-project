document.addEventListener('DOMContentLoaded', function() {
    const contacts = document.querySelectorAll('.contact-info');
    const selectedUserDetails = document.getElementById('selected_user_details');
    
    contacts.forEach(contact => {
        contact.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default behavior of anchor tags
            
            const userName = contact.querySelector('a').textContent;
            const userEmail = contact.querySelector('li:nth-child(2) a').textContent;
            const userPhone = contact.querySelector('li:nth-child(3) a').textContent;
            // Assuming other details like phone, etc., are also present in the HTML
            
            // Set the details of the selected user
            document.getElementById('selected_user_name').textContent = userName;
            document.getElementById('selected_user_email').textContent = userEmail;
            document.getElementById('selected_user_phone').textContent = userPhone;
            
            
            selectedUserDetails.style.display = 'block';
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('Upload_file').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = this;
        const formData = new FormData(form);

        fetch(form.action, {
            method: form.method,
            body: formData
        })
        .then(response => {
            if (response.ok) {
                Swal.fire('Success!', 'Data processed successfully!', 'success').then(() => {
                    window.location.href = '/users';
                });
            } else {
                return response.text();
            }
        })
        .then(errorMsg => {
            if (errorMsg) {
                Swal.fire('Error!', errorMsg, 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
