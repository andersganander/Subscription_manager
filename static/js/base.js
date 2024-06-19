// Initializes the materialize components
document.addEventListener('DOMContentLoaded', function() {
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
    M.updateTextFields();

    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    document.querySelectorAll('.edit-btn').forEach(function(button) {
        button.addEventListener('click', function() {
        var form = this.nextElementSibling;
        form.style.display = form.style.display === 'none' ? 'block' : 'none';
        });
    });
});