// To Do:
// Only allow arabic numbers and latin letters to be inputted into the form.

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const businessName = formData.get('business-name');
    const caption = formData.get('caption');

    const response = await fetch('/submit', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      const popup = document.createElement('div');

      popup.innerHTML = `Top Hashtags: <br><br> ${data.hashtags.join(' ')}`;
      popup.classList.add('popup');
      document.body.appendChild(popup);
      document.body.classList.add('blur');

      const closeButton = document.createElement('span');
        closeButton.textContent = '✕';
        closeButton.classList.add('close-btn');
        closeButton.addEventListener('click', () => {
          popup.remove();
          document.body.classList.remove('blur');
        });
      popup.appendChild(closeButton);

    } else {
      console.error('Form submission failed.');
    }
  });
});
