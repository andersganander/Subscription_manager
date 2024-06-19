const servicesDict = JSON.parse(document.getElementById('servicesData').textContent);
sortSelectEntries(document.getElementById('id_service')); // Sorts the services list alphabetically

// Function for populating price field when select is changed
document.getElementById('id_service').addEventListener('change', function () {
    const selectedName = this.options[this.selectedIndex].textContent; // Gets the selected service name
    const selectedPrice = servicesDict[selectedName]; // Gets the price using the service name as key
    document.getElementById('id_monthly_price').value = selectedPrice || ''; // Updates the price text field
    document.getElementById('id_subscription_name').value = selectedName || ''; // Updates the name field
});

// Sorts the select, function from: 
// https://stackoverflow.com/questions/1129216/sort-select-options-in-javascript
function sortSelectEntries(selItem) {
    let formerSel = selItem.value;
    let count = selItem.length;
    let options = new Array();
    for (var i = 0; i < count; i++)
        options[i] = selItem.options[i];
    options.sort((e1, e2) => e1.text > e2.text ? 1 : (e1.text < e2.text ? -1 : 0));
    for (i = 0; i < count; i++)
        selItem.options[i] = options[i];
    selItem.value = formerSel; 
}