
// html creation with js table
const administrator = document.getElementById("administrator");
const addBtn = document.createElement("button")

addBtn.id = "addBtn";
const addIcon = document.createElement('i');
addIcon.className = 'fa-solid fa-square-plus';
addBtn.textContent ="Add Template";
addBtn.appendChild(addIcon)

administrator.appendChild(addBtn);
const tableContainer = document.createElement('div');
tableContainer.className = "table_wrapper table_responsive";

const table = document.createElement("table");
table.className = "data_table";

const createTableHead = (text) => {
  const th = document.createElement("th");
  th.textContent = text;
  return th;
};

const tableHeads = ["Status", "Plantilla name", "Content", "", ""];

const headRow = document.createElement("tr");
headRow.append(...tableHeads.map(createTableHead));
table.append(headRow);

tableContainer.appendChild(table);
administrator.appendChild(tableContainer);

// Fetch data from the API
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
    // all data
    templateAds = data.template_ads
    templateAds.forEach((templateAd) => {
      const bodyRow = document.createElement("tr");
        const tdActive = document.createElement('td')
        const tdName = document.createElement('td')
        const tdContent = document.createElement('td')
        const tdEdit = document.createElement('td')
        const tdDelete = document.createElement('td')
        // edit btn
        const editBtn = document.createElement('button')
        editBtn.textContent = "Edit"
        editBtn.className = "btn btn-sm btn-primary"
        editBtn.setAttribute("id", "editBtn");
        const editIcon = document.createElement('i')
        editIcon.className = 'far fa-edit'
        tdEdit.appendChild(editBtn)
        editBtn.appendChild(editIcon)
        // delete btn
        const deleteBtn = document.createElement('button')
        deleteBtn.textContent = "Delete"
        deleteBtn.className = "btn btn-sm btn-primary"
        deleteBtn.setAttribute("id", "deleteBtn");
        const deleteIcon = document.createElement('i')
        deleteIcon.className = 'fas fa-trash-alt'
        tdDelete.appendChild(deleteBtn)
        deleteBtn.appendChild(deleteIcon)
        // body Rows
        bodyRow.appendChild(tdActive)
        bodyRow.appendChild(tdName)
        bodyRow.appendChild(tdContent)
        bodyRow.appendChild(tdEdit)
        bodyRow.appendChild(tdDelete)
        if(templateAd.active){
            tdActive.textContent = "active"
        }else{
            tdActive.textContent = "Inactive"
        }
        tdName.textContent += templateAd.name
        tdContent.textContent += templateAd.content.substring(0, 50) + '...';
        table.appendChild(bodyRow)
    });

  })
  .catch((error) => {
    console.error(error);
  });


