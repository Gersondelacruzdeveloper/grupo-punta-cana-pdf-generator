
// // Wait for the document to fully load
// document.addEventListener("DOMContentLoaded", function () {
//     const downloadPdfButtons = document.getElementsByClassName("download-pdf");
    
//     for (let i = 0; i < downloadPdfButtons.length; i++) {
//       const button = downloadPdfButtons[i];
  
//       button.addEventListener("click", function () {
//         // This code will run when a "download-pdf" button is clicked
//         console.log("Download PDF button clicked");
//         // You can call the generatePDF function here if needed
//         // generatePDF();
//       });
//     }
//   });
  

    // document.getElementById("download-pdf").addEventListener("click", function () {
    //     console.log("yes is been click")

    //   // Get the HTML template element by its ID
    //   const pdfTemplate = document.getElementById("pdf-template");

    //   // Create a configuration object for html2pdf.js
    //   const options = {
    //     margin: 10,
    //     filename: "generated-pdf.pdf",
    //     image: { type: "jpeg", quality: 0.98 },
    //     html2canvas: { scale: 2 },
    //     jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    //   };

    //   // Use html2pdf.js to generate the PDF from the HTML template
    //   html2pdf()
    //     .from(pdfTemplate)
    //     .set(options)
    //     .outputPdf(function (pdf) {
    //       // Save the PDF to a file or open it in a new tab
    //       pdf.save();
    //     });
//     });
