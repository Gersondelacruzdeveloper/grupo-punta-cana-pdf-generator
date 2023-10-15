
// Sample PDF data (you can load this dynamically from an API)
const pdfContainer = document.getElementById("pdf-container");
// Fetch data from the API
fetch('http://127.0.0.1:8000/api/pdf_list', {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
  },
})
  .then((response) => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error('Failed to fetch data');
    }
  })
  .then(async (data) => {
    const advertisements = data.advertisement;
    const userAdvertisements = advertisements[0].filter(advertisement => advertisement.user == userId);

    userAdvertisements.forEach((advertisement) => {
      // variables for templates
      dateCreated = advertisement.date_created
      // location = advertisement.location
      adsName = advertisement.name
      price = advertisement.price
      //HTML DIV
      const card = document.createElement("div");
      const generatePdfButton = document.createElement("button");
      generatePdfButton.classList.add("generate-pdf");
      generatePdfButton.classList.add("green-button");
      generatePdfButton.textContent = "Open PDF";
      card.classList.add("pdf-card");
      let content = advertisements[1].content;
      content = content.replace('${adsName}', adsName)
      content = content.replace('${price}', price)
      card.innerHTML = content
      card.appendChild(generatePdfButton)
      pdfContainer.appendChild(card)
      // generate pdf when btn is click
      generatePdfButton.addEventListener('click', function(){
      const pdf = new jsPDF();
      pdf.fromHTML(content.replace('${adsName}', adsName));
      pdf.save()
    });
    });
  })
  
  .catch((error) => {
    console.error(error);

  });
