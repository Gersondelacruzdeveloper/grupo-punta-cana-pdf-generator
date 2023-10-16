function fetchDataAndPopulateTable() {
    fetch('http://127.0.0.1:8000/api/admin_list', {
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
        // Clear the table before populating it
        while (table.firstChild) {
          table.removeChild(table.firstChild);
        }
  
        const templateAds = data.template_ads;
        const templateInvoices = data.template_invoiceses;
        const templateBoardings = data.template_boardings;
  
        templateAds.forEach((templateAd) => {
          table.appendChild(createTableRow(templateAd));
        });
  
        templateInvoices.forEach((templateInvoice) => {
          table.appendChild(createTableRow(templateInvoice));
        });
  
        templateBoardings.forEach((templateBoarding) => {
          table.appendChild(createTableRow(templateBoarding));
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }