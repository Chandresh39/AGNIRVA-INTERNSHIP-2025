// This code waits until the HTML document is fully loaded before running
document.addEventListener("DOMContentLoaded", () => {
    // Create a new button element
    const button = document.createElement("button");
    // Set the button's text content
    button.textContent = "Click Me!";

    // Add an event listener to the button for the 'click' event
    button.addEventListener("click", () => {
        // Show an alert when the button is clicked
        alert("Thanks for visiting my portfolio!");
    });

    // Append the button to the body of the document
    document.body.appendChild(button);
});
