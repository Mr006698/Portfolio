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
        menu.style.height = "200px"; // This will need adjusting if menu items added.
    }
    else {
        menu.style.height = "0px";
    }
}

// Close the dropdown if the user clicks outside of it
window.addEventListener('click', function(event) {
    console.log(event.target)
    if (!event.target.matches(".fa-bars")) {
        var menu = document.getElementById("menu-dropdown");
        menu.style.padding = "0em 0em 0em 0em";
        menu.style.height = "0px";
    }
})

// window.onscroll = () => {
//     sections.forEach(sec => {
//         let top = window.scrollY;
//         let offset = sec.offsetTop - 250;
//         let height = sec.offsetHeight;
//         let id = sec.getAttribute('id');

//         if(top >= offset && top < offset + height) {
//             navLinks.forEach(links => {
//                 links.classList.remove('active');
//                 document.querySelector('li a[href*=' + id + ']').classList.add('active');
//             });
//         };
//     })
// };

// Scroll to the section when the user clicks the link
function gotoByScroll(id) {
    let element = document.getElementById(id);
    element.scrollIntoView({behavior: "smooth"});
}