// Sample PDF data (you can load this dynamically from an API)
import {createPdfCard} from './functions/CreateCard.js';

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
    // advertisements
    const advertisements = data.advertisement;
    const advertisementsTemplate = advertisements[1].content
    // invoice
    const invoices = data.invoices;
    const invoiceTemplate = invoices[1].content
    // Process Boarding pass here

    // search for the login user
    const userAdvertisements = advertisements[0].filter(advertisement => advertisement.user == userId);
    const userInvoices = invoices[0].filter(invoice => invoice.user == userId);

    // Process userAdvertisements
    userAdvertisements.forEach((advertisement) => {
      createPdfCard(advertisement, advertisementsTemplate); // Use the appropriate content template
    });
    // Process userInvoices
    userInvoices.forEach((invoice) => {
      createPdfCard(invoice, invoiceTemplate); // Use the appropriate content template
    });

    // Process Boarding pass here

  })
  .catch((error) => {
    console.error(error);
  });
