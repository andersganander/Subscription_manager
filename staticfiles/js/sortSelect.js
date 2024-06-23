// Sorts the select, function from: 
// https://stackoverflow.com/questions/1129216/sort-select-options-in-javascript
function sortSelectEntries(selItem) {
    const formerSel = selItem.value;
    const count = selItem.length;
    let options = [];
    for (let i = 0; i < count; i++)
        options[i] = selItem.options[i];
    options.sort((e1, e2) => e1.text > e2.text ? 1 : (e1.text < e2.text ? -1 : 0));
    for (i = 0; i < count; i++)
        selItem.options[i] = options[i];
    selItem.value = formerSel; 
}