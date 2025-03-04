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

        // Clear input
        questionInput.value = '';

        // Show loading indicator
        loadingIndicator.classList.remove('d-none');

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Create new chat entry
            const chatEntry = document.createElement('div');
            chatEntry.className = 'chat-entry';
            
            // Add question
            const questionDiv = document.createElement('div');
            questionDiv.className = 'question mb-2';
            questionDiv.innerHTML = `
                <i class="bi bi-person-circle"></i>
                <span>${question}</span>
            `;
            
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
            
            chatEntry.appendChild(questionDiv);
            chatEntry.appendChild(answerDiv);
            
            // Add to chat container
            chatContainer.appendChild(chatEntry);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while processing your request.');
        } finally {
            loadingIndicator.classList.add('d-none');
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
