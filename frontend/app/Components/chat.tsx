import React, { useState} from 'react'

 
export function Chat() {
    const [prompt, setPrompt] = useState('');
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: { preventDefault: () => void; }) => {
        e.preventDefault();
        setLoading(true);

        try 
        {
            const response = await fetch('http://localhost:8000/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt}),
            });

            if (!response.ok) {
                throw new Error('Error while fetching data from the server.');
            }

            const data = await response.json();
            setResult(data); //saves the answer in the state
        } catch (error) {
            console.error('Error while connecting to the server:', error);
            setResult('Fehler bei der Serververbindung: ' + error);
        } finally {
            setLoading(false);
        }
    };

    return (
    <div style={{ padding: '2rem' }}>
      <h1>LLM Wiki Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Frage eingeben..."
          style={{ padding: '0.5rem', width: '300px', marginRight: '1rem' }}
        />
        <button type="submit" disabled={loading} style={{ padding: '0.5rem 1rem' }}>
          {loading ? 'Lädt...' : 'Senden'}
        </button>
      </form>

      <div style={{ marginTop: '2rem' }}>
        <h3>Antwort:</h3>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default Chat;