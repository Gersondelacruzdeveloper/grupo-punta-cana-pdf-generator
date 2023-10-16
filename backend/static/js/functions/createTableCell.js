// Helper function to create a table cell
function createTableCell(text) {
    const cell = document.createElement('td');
    cell.textContent = text;
    return cell;
  }

  // Helper function to create a table heading cell (th)
function createTableHeading(text) {
    const th = document.createElement('th');
    th.textContent = text;
    return th;
}
  
  export {createTableCell, createTableHeading}