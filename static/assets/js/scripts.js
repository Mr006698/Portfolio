// Open the development modal on load
devModal = new bootstrap.Modal(document.getElementById("message-modal"), {});
document.onreadystatechange = function() {
    devModal.show();
}

// Toggle the menu when the user clicks the button
function openMenu() {
    menu = document.getElementById("menu-dropdown");
    height = menu.offsetHeight;
    if (height == 0) {
        menu.style.height = "145px"; // This will need adjusting if menu items added.
    }
    else {
        menu.style.height = "0px";
    }
}

// Close the dropdown if the user clicks outside of it
window.addEventListener('click', function(event) {
    if (!event.target.matches(".fa-bars")) {
        var menu = document.getElementById("menu-dropdown");
        menu.style.padding = "0em 0em 0em 0em";
        menu.style.height = "0px";
    }
})

// Activate menu link on scroll
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('li a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 250;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('li a[href*=' + id + ']').classList.add('active');
            });
        };
    })
};

// Scroll to the section when the user clicks the link
function gotoByScroll(id) {
    let element = document.getElementById(id);
    element.scrollIntoView({behavior: "smooth"});
}

// JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll(".validate-form");
    const fields = document.querySelectorAll(".form-control");

    // Get the submit button so we can disable it to stop multiple clicks
    const submitBtn = document.getElementById("submit-button");
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        event.preventDefault();
        event.stopPropagation();

        submitBtn.disabled = true;

        // Validate with server
        const formData = new FormData(form);
        fetch("/submit", {
            method: "POST",
            body: formData
        }).then((response) => response.json()).then((result) => {
            if (result['ok']) {
                Array.from(fields).forEach(field => {
                    field.classList.remove("is-valid");
                    field.classList.remove("is-invalid");
                });

                form.reset(); // Clear the form
                const messageTitle = document.querySelector('.message-title');
                const messageContent = document.querySelector('.message-content');
                messageTitle.textContent = 'Message Sent';
                messageContent.textContent = result['success'];
                devModal.show()

            } else {
                Array.from(fields).forEach(field => {
                    if (result["errors"][field.id]) {
                        field.classList.remove("is-valid");
                        field.classList.add("is-invalid");
                        const errorMsg = document.getElementById("error-" + field.id);
                        errorMsg.childNodes[0].nodeValue = result["errors"][field.id];

                    } else {
                        field.classList.remove("is-invalid");
                        field.classList.add("is-valid");
                        // const errorMsg = document.getElementById("error-" + field.id);
                        // errorMsg.childNodes[0].nodeValue = "Success";
                    }
                });
            }

            // Enable submit button
            submitBtn.disabled = false;
        });

      }, false)
    })
  })()