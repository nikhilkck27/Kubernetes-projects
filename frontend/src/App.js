import React, { useState, useEffect } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    fetch('/items')
      .then(res => res.json())
      .then(data => setItems(data.items));
  }, []);

  const addItem = () => {
    fetch('/items', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name }),
    })
      .then(res => res.json())
      .then(item => setItems([...items, item]));
  };

  const deleteItem = (id) => {
    fetch(`/items/${id}`, { method: 'DELETE' })
      .then(() => setItems(items.filter(item => item.id !== id)));
  };

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} <button onClick={() => deleteItem(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <input value={name} onChange={e => setName(e.target.value)} />
      <button onClick={addItem}>Add Item</button>
    </div>
  );
}

export default App;
