import React, { useState } from 'react';

function SearchBar({ onSubmit }) {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input) {
      onSubmit(input);
      setInput('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ textAlign: 'center', marginTop: '20px' }}>
      <input
        type="text"
        placeholder="Enter YouTube video link"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ padding: '10px', width: '70%' }}
      />
      <button type="submit" style={{ padding: '10px 20px', marginLeft: '10px' }}>
        Get Recipe
      </button>
    </form>
  );
}

export default SearchBar;