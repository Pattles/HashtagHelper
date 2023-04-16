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
      popup.innerHTML = `Top hashtags: ${data.hashtags.join(' ')}`;
      popup.classList.add('popup');
      document.body.appendChild(popup);

      // This is what makes you wait 3sec before it auto-closes the popup.
      setTimeout(() => {
        popup.remove();
      }, 6000);
    } else {
      console.error('Form submission failed.');
    }
  });
});
