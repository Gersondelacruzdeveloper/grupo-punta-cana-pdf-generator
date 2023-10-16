
import {createTableCell, createTableHeading} from './functions/createTableCell.js'
import {createButtonWithIcon} from './functions/createButtonWithIcon.js'
import {createTableRow} from './functions/createTableRow.js'
import {csrftoken} from './functions/csrftoken.js'
// HTML creation with JavaScript for the table
const administrator = document.getElementById('administrator');
// Create the "Add Template" button
const btnContainer = document.createElement('div');
btnContainer.className = 'center-btn';
const addBtn = createButtonWithIcon('Add Template', 'fa-solid fa-square-plus');
addBtn.id = 'addBtn';
btnContainer.appendChild(addBtn);
administrator.appendChild(btnContainer);

const tableContainer = document.createElement('div');
tableContainer.className = 'table_wrapper table_responsive';

const table = document.createElement('table');
table.className = 'data_table';

// Create the table header
const tableHeads = ['Status', 'Plantilla name', 'Content', '', ''];
const headRow = document.createElement('tr');
headRow.append(...tableHeads.map(createTableHeading));
table.appendChild(headRow);

tableContainer.appendChild(table);
administrator.appendChild(tableContainer);
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

// You can call this function whenever you need to fetch and populate the table
fetchDataAndPopulateTable();

// You can call this function whenever you need to fetch and populate the table
fetchDataAndPopulateTable();
  
   const modal = document.getElementById('modal');
  const closeModalButton = document.getElementById('closeModal'); // Add this line

  // btns add
  addBtn.addEventListener('click', function(){
    modal.style.display = 'block';
  });

  modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    
    }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && modal.style.display === 'block') {
      modal.style.display = 'none';
  }
});

closeModalButton.addEventListener('click', () => { // Add this event listener
  modal.style.display = 'none';
});

const templateForm = document.getElementById("addTemplateForm");
templateForm.addEventListener("submit", function(event){
  event.preventDefault(); // Prevent the default form submission
  // process form
  console.log('form submited')
  // Get from admin list 

    // Get the values from the form fields
    const templateName = document.getElementById("templateName").value;
    const templateContent = document.getElementById("templateContent").value;
    const templateType = document.getElementById("templateType").value;
    const templateActive = document.getElementById("templateActive").checked;
  
    const data = {
      "name": templateName,
      "content": templateContent,
      "type": templateType,
      "active": templateActive
    };

  fetch('http://127.0.0.1:8000/api/add_template', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(result => {
      console.log('Response->:', result);
      modal.style.display = 'none'
      fetchDataAndPopulateTable();
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
})




