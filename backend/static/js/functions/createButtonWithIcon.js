// Helper function to create a button with an icon
function createButtonWithIcon(text, iconClass) {
  const button = document.createElement('button');
  button.textContent = text;
  button.className = 'btn btn-sm btn-primary';
  const icon = document.createElement('i');
  icon.className = iconClass;
  button.appendChild(icon);
  return button;
}
export {createButtonWithIcon}