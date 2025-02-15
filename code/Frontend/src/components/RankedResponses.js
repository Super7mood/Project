import React, { useState, useEffect } from 'react';
import './RankedResponses.css';

function RankedResponses() {
    const [responses, setResponses] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [selectedType, setSelectedType] = useState('number');

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            setError(null);
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: "Who was the president of the USA in 2008?" })
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                // Format or handle responses if they are objects
                const formattedResponses = data.map(item => ({
                    model: item.model,
                    response: item.response?.text || item.response, // Assuming response might be an object with a text property
                    score: typeof item.score === 'object' ? JSON.stringify(item.score) : item.score, // Convert score object to string if it's an object
                    type: item.type // Assuming there's a 'type' property to determine response category
                }));
                setResponses(formattedResponses);
            } catch (err) {
                setError('Failed to fetch data: ' + err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    const filteredResponses = responses.filter(response => response.type === selectedType);

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div className="ranked-responses-container">
            <div className="tab-bar">
                <button onClick={() => setSelectedType('number')}>Number</button>
                <button onClick={() => setSelectedType('word')}>Word</button>
                <button onClick={() => setSelectedType('phrase')}>Phrase</button>
                <button onClick={() => setSelectedType('sentence')}>Sentence</button>
                <button onClick={() => setSelectedType('paragraph')}>Paragraph</button>
            </div>

            {filteredResponses.length > 0 ? filteredResponses.map((item, index) => (
                <div key={index} className="response-item">
                    <h3>{item.model} Response:</h3>
                    <p>{item.response}</p>
                    <p>Score: {item.score}</p>
                </div>
            )) : <div>No data available</div>}
        </div>
    );
}

export default RankedResponses;
