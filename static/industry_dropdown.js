// This doesn't work for some reason ffs


// List of all industries
const industries = [
    'Accounting',
    'Airbnb',
    'Art',
    'Architect',
    'Breeding',
    'Book Store',
    'Brewing',
    'Butchering',
    'Car Insurance',
    'Car Rentals',
    'Car Repairs',
    'Casino',
    'Chiropractor',
    'Church',
    'Civil Engineering',
    'Computer Repairs',
    'Concert',
    'Crop Production',
    'Custom furniture',
    'Data Infrastructure',
    'Dentist',
    'Dining',
    'Discount furniture',
    'Dumpster',
    'Education',
    'Electrical Engineering',
    'Equipment Rentals',
    'Farming',
    'Fashion',
    'Festival',
    'Fishing Guide',
    'Financial Advising',
    'Garden Center',
    'Healthcare',
    'Investor',
    'Leatherworking',
    'Library',
    'Lodging',
    'Masonry',
    'Magazines',
    'Manufacturing',
    'Marketing Agency',
    'Mechanical Engineering',
    'Museum',
    'News',
    'Office Support Services',
    'Outdoor Services',
    'Painting',
    'Phone Repairs',
    'Plumbing',
    'Printing',
    'Produce',
    'Radio',
    'Recycling',
    'Realtor',
    'Resort',
    'Roofing',
    'Sanitation',
    'Self storage',
    'Shop Rentals',
    'Sporting Event',
    'Steak House',
    'Supermarket',
    'Taxidermy',
    'Theater',
    'Theme park',
    'Training',
    'Trucking',
    'Tutoring',
    'Warehousing',
    'Welding',
    'YMCA'
  ];
  
  // Get the input field and dropdown
  const industryInput = document.getElementById('industry');
  const industryDropdown = document.getElementById('industry-dropdown');
  
  // Create a function to update the dropdown options based on user input
  function updateDropdown() {
    // Clear existing dropdown options
    industryDropdown.innerHTML = '';
  
    // Get user input and filter industries list
    const industry = industryInput.value.toLowerCase();
    const filteredIndustries = industries.filter((item) =>
      item.toLowerCase().includes(industry)
    );
  
    // Add filtered industries to dropdown options
    filteredIndustries.forEach((item) => {
      const option = document.createElement('option');
      option.value = item;
      industryDropdown.appendChild(option);
    });
  
    // Show the dropdown if there are filtered industries, otherwise hide it
    if (filteredIndustries.length > 0) {
      industryDropdown.style.display = 'block';
    } else {
      industryDropdown.style.display = 'none';
    }
  }
  
  // Update the dropdown options when the user types in the input field
  industryInput.addEventListener('input', updateDropdown);  