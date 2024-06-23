const servicesDict = JSON.parse(document.getElementById('servicesData').textContent);
sortSelectEntries(document.getElementById('id_service')); // Sorts the services list alphabetically

// Function for populating price field when select is changed
document.getElementById('id_service').addEventListener('change', function () {
    const selectedName = this.options[this.selectedIndex].textContent; // Gets the selected service name
    const selectedPrice = servicesDict[selectedName]; // Gets the price using the service name as key
    document.getElementById('id_monthly_price').value = selectedPrice || ''; // Updates the price text field
    document.getElementById('id_subscription_name').value = selectedName || ''; // Updates the name field
});
