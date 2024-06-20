document.addEventListener('DOMContentLoaded', function () {
    // Initializing materialize elemets  
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, {
        format: 'yyyy-mm-dd'
    });
    let tooltips = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(tooltips);

    // Sort categories in select
    sortSelectEntries(document.getElementById('id_subscription_category')); // Sorts the services list alphabetically

    // event listener for link to clear reminder input fields
    var resetLink = document.getElementById('clear_reminder');

    // Add click event listener to the link
    resetLink.addEventListener('click', function (event) {
        // Prevent the default action of the link
        event.preventDefault();

        // Get the text fields by their IDs
        var textField1 = document.getElementById('id_reminder_date');
        var textField2 = document.getElementById('id_reminder_notes');

        // Reset the values of the text fields
        textField1.setAttribute('value', '');
        textField2.setAttribute('value', '');
    });

});