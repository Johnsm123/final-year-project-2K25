document.addEventListener('DOMContentLoaded', () => {
    // Assign event listeners to buttons
    const fleetButton = document.getElementById('fleet-btn');
    const weatherButton = document.getElementById('weather-btn');
    const mlButton = document.getElementById('ml-btn');
    const indexButton = document.getElementById('index-btn'); // New button to open index.html

    if (fleetButton) {
        fleetButton.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent default link behavior
            window.open('https://example.com/fleet-management', '_blank'); // Open Fleet Management link in a new tab
        });
    }

    if (weatherButton) {
        weatherButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.open('https://example.com/weather-monitoring', '_blank'); // Open Weather Monitoring link in a new tab
        });
    }

    if (mlButton) {
        mlButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.open('https://example.com/machine-learning', '_blank'); // Open Machine Learning link in a new tab
        });
    }

    // New event listener for index button to open index.html in a new tab
    if (indexButton) {
        indexButton.addEventListener('click', (e) => {
            e.preventDefault();
            // Open the index page in a new tab using the correct URL path
            window.open('/index/', '_blank'); // Ensure this URL is correct in your URLs configuration
        });
    }

    // Adding animation to the title letters
    const keys = document.querySelectorAll('.key');
    keys.forEach((key) => {
        key.addEventListener('mouseover', () => {
            key.style.transform = 'scale(1.2)'; // Scale up on hover
        });
        key.addEventListener('mouseout', () => {
            key.style.transform = 'scale(1)'; // Reset scale when mouse leaves
        });
    });

    // Dynamically fetch and set the background image
    const backgroundContainer = document.getElementById('background-container');
    if (backgroundContainer) {
        fetch(`/background/${backgroundContainer.dataset.projectId}/`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.blob();
            })
            .then((blob) => {
                const url = URL.createObjectURL(blob);
                backgroundContainer.style.backgroundImage = `url(${url})`;
            })
            .catch((error) => {
                console.error('Error fetching background image:', error);
                // Optional: Set a default background image if fetching fails
                backgroundContainer.style.backgroundImage = `url('/static/images/default-background.jpg')`;
            });
    }
});
