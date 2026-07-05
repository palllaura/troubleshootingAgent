function sendMessage() {
    const userInput = document.getElementById("userInput");
    const userMessage = userInput.value.trim();

    if (userMessage === "") {
        return;
    }

    addMessage("You", userMessage);

    userInput.value = "";

    respondToMessage(userMessage);
}

function respondToMessage(userMessage) {
    setTimeout(function () {
        addMessage("Chatbot", getBotResponse(userMessage));
    }, 1000);
}

function addMessage(sender, message) {
    const messages = document.getElementById("messages");

    const messageDiv = document.createElement("div");
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;

    messages.appendChild(messageDiv);

    messages.scrollTop = messages.scrollHeight;
}

function quickReply(message) {
    document.getElementById("userInput").value = message;
    sendMessage();
}

function getBotResponse(message) {
    const responses = {
        "hello": "Hi! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name?": "I'm your friendly troubleshooting chatbot.",
        "goodbye": "Goodbye! Have a great day!"
    };

    return responses[message.toLowerCase()] ||
        "Sorry, I didn't understand that. Could you rephrase?";
}