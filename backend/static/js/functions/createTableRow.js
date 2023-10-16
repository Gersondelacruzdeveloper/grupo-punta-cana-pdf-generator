import {createTableCell} from './createTableCell.js'
import {createButtonWithIcon} from './createButtonWithIcon.js'

// Helper function to create a row for the table
function createTableRow(templateAd) {
    const row = document.createElement('tr');
    
    const tdActive = createTableCell(templateAd.active ? 'Active' : 'Inactive');
    const tdName = createTableCell(templateAd.name);
    const tdContent = createTableCell(templateAd.content.substring(0, 50) + '...');
    
    const tdEdit = createTableCell('');
    tdEdit.appendChild(createButtonWithIcon('Edit', 'far fa-edit'));
    
    const tdDelete = createTableCell('');
    tdDelete.appendChild(createButtonWithIcon('Delete', 'fas fa-trash-alt'));
    
    row.appendChild(tdActive);
    row.appendChild(tdName);
    row.appendChild(tdContent);
    row.appendChild(tdEdit);
    row.appendChild(tdDelete);
    
    return row;
  }
  export {createTableRow}