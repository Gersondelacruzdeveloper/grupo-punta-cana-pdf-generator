function createPdfCard(data, contentTemplate) {
   const pdfContainer = document.getElementById("pdf-container");
    const { date, name, price, issue_date, description, subtotal, totalAmount, tax, invoice_number} = data;
    let content = contentTemplate;
    // Loop through the keys in the data object and replace placeholders
    for (const key in data) {
      if (data.hasOwnProperty(key)) {
        const placeholder = `{${key}}`;
        const value = data[key] || '';
        content = content.replace(placeholder, value);
      }
    }
    // varialbes for div html
    const card = document.createElement("div");
    const generatePdfButton = document.createElement("button");
    generatePdfButton.classList.add("generate-pdf");
    generatePdfButton.classList.add("green-button");
    generatePdfButton.textContent = "Open PDF";
    card.classList.add("pdf-card");
    card.innerHTML = content;
    card.appendChild(generatePdfButton);
    pdfContainer.appendChild(card);
  
  // when button is click it generate the pdf
    generatePdfButton.addEventListener('click', function () {
      const pdf = new jsPDF();
      pdf.fromHTML(content);
      pdf.save();
    });
  }

export {createPdfCard};
  