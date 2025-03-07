document.addEventListener('DOMContentLoaded', function() {
    const questionForm = document.getElementById('questionForm');
    const questionInput = document.getElementById('questionInput');
    const chatContainer = document.getElementById('chatContainer');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const clearHistoryBtn = document.getElementById('clearHistory');

    questionForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const question = questionInput.value.trim();
        if (!question) return;

        // Clear input and disable
        questionInput.value = '';
        questionInput.disabled = true;

        // Show loading indicator
        loadingIndicator.classList.remove('d-none');

        // Create and display question immediately
        const chatEntry = document.createElement('div');
        chatEntry.className = 'chat-entry';

        const questionDiv = document.createElement('div');
        questionDiv.className = 'question mb-2';
        questionDiv.innerHTML = `
            <i class="bi bi-person-circle"></i>
            <span>${question}</span>
        `;
        chatEntry.appendChild(questionDiv);
        chatContainer.appendChild(chatEntry);

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question }),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'An error occurred');
            }

            // Add answer
            const answerDiv = document.createElement('div');
            answerDiv.className = 'answer';

            let sourcesHtml = '';
            if (data.sources && data.sources.length > 0) {
                sourcesHtml = `
                    <div class="sources mt-2">
                        <h6>Sources:</h6>
                        <ul class="list-unstyled">
                            ${data.sources.map(source => `
                                <li>
                                    <a href="${source.url}" target="_blank">${source.title}</a>
                                    <p class="source-snippet">${source.snippet}</p>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                `;
            }

            answerDiv.innerHTML = `
                <i class="bi bi-robot"></i>
                <div class="answer-content">
                    ${data.answer}
                    ${sourcesHtml}
                </div>
            `;

            chatEntry.appendChild(answerDiv);

            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;

        } catch (error) {
            // Create error message element
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-danger mt-3';

            // Check if it's a rate limit error
            if (error.message.includes('high traffic') || error.message.includes('busy')) {
                errorDiv.innerHTML = `
                    <i class="bi bi-exclamation-triangle"></i>
                    ${error.message}<br>
                    <small class="text-muted">The system is experiencing high demand. Your request will be retried automatically.</small>
                `;
            } else {
                errorDiv.innerHTML = `
                    <i class="bi bi-exclamation-circle"></i>
                    ${error.message || 'An error occurred while processing your request.'}
                `;
            }

            chatEntry.appendChild(errorDiv);

            // Auto-remove error message after 5 seconds
            setTimeout(() => {
                errorDiv.remove();
            }, 5000);

        } finally {
            loadingIndicator.classList.add('d-none');
            questionInput.disabled = false;
            questionInput.focus();
        }
    });

    clearHistoryBtn.addEventListener('click', async function() {
        try {
            const response = await fetch('/clear', {
                method: 'POST',
            });

            if (response.ok) {
                chatContainer.innerHTML = '';
            } else {
                throw new Error('Failed to clear history');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to clear chat history');
        }
    });
});