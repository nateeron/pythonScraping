

var elements = document.querySelectorAll('.mZ1OWk');
var sum ;
elements.forEach(function(element) {
    
    console.log(element)
    var Name = element.querySelector('.DWVWOJ');
    var price = element.querySelector('.nW_6Oi');
    var date = element.querySelector('.Shopee-drawer__contents');

    console.log(date)

    // // Access the text content of the found element
    var NametextContent = Name.textContent;
    console.log(NametextContent);
    var pricetextContent = price.textContent;
    console.log(pricetextContent);
    console.log(pricetextContent.replace('฿',''))
    var price = parseFloat(pricetextContent.replace('฿', ''));
    sum += price
    console.log(NametextContent,',',price)

});
console.log(sum)
//---------------------------------------------------------
var elements = document.querySelectorAll('.mZ1OWk');
var csvContent = "Name,Price\n"; // Header row

elements.forEach(function(element) {
    var Name = element.querySelector('.DWVWOJ');
    var price = element.querySelector('.nW_6Oi');
    var date = element.querySelector('.Shopee-drawer__contents');
    console.log(date)
    if (Name && price) {
        var NametextContent = Name.textContent.trim().replace(',',' ');
        var pricetextContent = price.textContent.trim().replace('฿','');

        // Append row to CSV content
        csvContent += NametextContent + "," + pricetextContent + "\n";
    }
});

// Create a blob with the CSV content
var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8' });

// Create a temporary anchor element
var a = document.createElement('a');
a.href = window.URL.createObjectURL(blob);
a.download = 'data.csv'; // Set filename

// Trigger a click event to simulate download
a.click();



