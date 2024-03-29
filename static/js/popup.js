// To Do:
// * Only allow arabic numbers and latin letters to be inputted into the form.
// * Send a notice of error to our logs, upon an error & notify the user

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

      popup.classList.add('popup');

      // Close button
      const closeButton = document.createElement('span');
        closeButton.textContent = '✕';
        closeButton.classList.add('close-btn');
        closeButton.addEventListener('click', () => {
          popup.remove();
          document.body.classList.remove('blur');
          document.body.style.pointerEvents = 'auto'; // Makes it so the page can be interacted with again
        });
      popup.appendChild(closeButton);
      closeButton.style.visibility = 'visible';

      // Hashtags element
      const hashtagsText = document.createElement('p');
      hashtagsText.classList.add('hashtags-text');
      hashtagsText.innerHTML = `Top Hashtags: <br><br> ${data.hashtags.join(' ')}`;
      popup.appendChild(hashtagsText);

      // Copy button
      const copyButton = document.createElement('button');
      copyButton.classList.add('copy-button');
      copyButton.textContent = 'Copy Hashtags';
      copyButton.addEventListener('click', () => {
        const hashtags = data.hashtags.join(' '); // Concatenate the hashtags with a space
        // Use the appropriate method to copy the hashtags text to the clipboard
        navigator.clipboard.writeText(hashtags)
          .then(() => {
            console.log('Hashtags copied to clipboard');
            copyButton.textContent = 'Copied!';
            copyButton.classList.add('clicked');

            setTimeout(() => {
              copyButton.classList.remove('clicked');
              copyButton.textContent = 'Copy Hashtags';
            }, 3000);
          })
          .catch((error) => {
            console.error('Failed to copy hashtags:', error);
          });
      });

      popup.appendChild(copyButton);
      copyButton.style.visibility = 'visible';
      


      // Everything else
      document.body.appendChild(popup);
      document.body.style.pointerEvents = 'none'; // Preventing page to be interacted with
      popup.style.pointerEvents = 'auto'; // With only popup being able to be interacted with
      document.body.classList.add('blur');

    } else {
      console.error('Form submission failed.');
    }
  });
});
