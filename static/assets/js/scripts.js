// Open the development modal on load
devModal = new bootstrap.Modal(document.getElementById("message-modal"), {});
document.onreadystatechange = function() {
    devModal.show();
}
