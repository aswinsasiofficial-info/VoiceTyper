// ===============================
// Voice Recognition (Web Speech)
// ===============================

// Browser support check
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
  alert("Speech recognition not supported. Use Google Chrome.");
}

// Create recognition instance
const recognition = new SpeechRecognition();
recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = "en-IN";

// Elements (must exist in HTML)
const micBtn = document.getElementById("micBtn");
const transcriptBox = document.getElementById("transcript");
const hiddenContent = document.getElementById("hiddenContent");

let isRecording = false;

// When speech is recognized
recognition.onresult = function (event) {
  let finalText = "";

  for (let i = event.resultIndex; i < event.results.length; i++) {
    finalText += event.results[i][0].transcript;
  }

  // Show text on UI
  transcriptBox.innerText = finalText;

  // Send text to Django form field
  hiddenContent.value = finalText;
};

// Error handling
recognition.onerror = function (event) {
  console.error("Speech recognition error:", event.error);
};

// Start / Stop on mic click
micBtn.addEventListener("click", function () {
  if (!isRecording) {
    recognition.start();
    micBtn.classList.add("active");
    isRecording = true;
  } else {
    recognition.stop();
    micBtn.classList.remove("active");
    isRecording = false;
  }
});
