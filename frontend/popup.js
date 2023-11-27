// Function to make a POST API request to calculate safety percentage
async function calculateSafetyPercentage(url) {
  const requestBody = { url: url };

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }

    const data = await response.json();

    const messageElement = document.getElementById("message");
    if (data?.pred) {
      messageElement.textContent = data.pred;
    } else {
      messageElement.textContent = "Error while fetching data";
    }
  } catch (error) {
    const messageElement = document.getElementById("message");
    if (messageElement) {
      messageElement.textContent = "Error while fetching data";
    }
  }
}

// Get the current tab's URL and calculate safety percentage
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  const currentTab = tabs[0];
  const tabUrl = currentTab.url;
  console.log(tabUrl);
  // Call the function to calculate safety percentage
  calculateSafetyPercentage(tabUrl);
});
