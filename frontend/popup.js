// Function to detect fake websites based on URL keywords
function detectFakeWebsite(url) {
  // Define a list of keywords commonly found in fake websites
  const fakeKeywords = ["phishing", "scam", "fake", "malware"];

  // Convert the URL to lowercase for case-insensitive matching
  const lowercaseUrl = url.toLowerCase();

  // Check if any of the fake keywords are present in the URL
  for (const keyword of fakeKeywords) {
    if (lowercaseUrl.includes(keyword)) {
      return true; // This might be a fake website
    }
  }

  return false; // No fake keywords found
}

// Get the current tab's URL and check if it's a fake website
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  const currentTab = tabs[0];
  const tabUrl = currentTab.url;

  if (detectFakeWebsite(tabUrl)) {
    // If it's a potential fake website, show a warning message
    document.getElementById("message").textContent =
      "This website may be fake or unsafe!";
  } else {
    // Otherwise, display a message indicating it's not a fake website
    document.getElementById("message").textContent = "This website seems safe.";
  }
});
