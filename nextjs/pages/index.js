import { useState } from 'react';

export default function Home() {
  const [response, setResponse] = useState(null);

  const handleCluster = async () => {
    const res = await fetch('/api/cluster', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ inputs: ['Idea 1', 'Idea 2', 'Idea 3'] })
    });
    const data = await res.json();
    setResponse(data);
  };

  return (
    <div>
      <h1>Next.js + Flask</h1>
      <button onClick={handleCluster}>Generate Clusters</button>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
}
