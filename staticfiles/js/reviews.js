document.addEventListener('DOMContentLoaded', function () {
    const deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;  // Button that triggered the modal
        const deleteUrl = button.getAttribute('data-review-url');  // Extract the review URL
        const confirmLink = deleteModal.querySelector('#deleteConfirm');
        confirmLink.href = deleteUrl;  // Set the href of the confirm button
    });
});
