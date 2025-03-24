document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const questionInput = chatForm.querySelector('textarea[name="question"]');
    const chatContainer = document.getElementById('chat-container');
    const loadingIndicator = document.getElementById('loading');
    const errorDisplay = document.getElementById('error');

    // Configure marked options
    marked.setOptions({
        breaks: true,
        gfm: true,
        sanitize: false
    });

    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'ai-message'}`;
        
        if (isUser) {
            messageDiv.textContent = content;
        } else {
            messageDiv.innerHTML = marked.parse(content);
        }
        
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const question = questionInput.value.trim();
        if (!question) return;

        // Clear previous error
        errorDisplay.style.display = 'none';
        errorDisplay.textContent = '';

        // Add user message
        addMessage(question, true);
        questionInput.value = '';

        // Show loading indicator
        loadingIndicator.classList.add('active');

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `question=${encodeURIComponent(question)}`
            });

            const data = await response.json();

            if (data.status === 'success') {
                // Add AI message
                addMessage(data.messages[data.messages.length - 1].content);
            } else {
                throw new Error(data.message || 'An error occurred');
            }
        } catch (error) {
            errorDisplay.textContent = error.message;
            errorDisplay.style.display = 'block';
        } finally {
            loadingIndicator.classList.remove('active');
        }
    });

    // Handle Enter key
    questionInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });

    // Scroll to bottom on load
    chatContainer.scrollTop = chatContainer.scrollHeight;
}); 