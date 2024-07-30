// Get the featured cars section
const featuredCarsSection = document.querySelector('.featured-cars');

// Get the buttons for each car item
const carButtons = featuredCarsSection.querySelectorAll('.car-item button');

// Add event listener to each button
carButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Get the car information from the button's parent element
    const carInfo = button.parentElement.querySelector('.car-info').textContent;
    
    // Display the car information in an alert
    alert(carInfo);
  });
});
