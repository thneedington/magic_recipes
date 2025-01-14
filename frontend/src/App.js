import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import RecipeDisplay from './components/RecipeDisplay';
import './App.css';

function App() {
  const [recipe, setRecipe] = useState(null);

  const fetchRecipe = async (youtubeLink) => {
    try {
      const response = await fetch('http://<your-backend-url>/api/get-recipe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: youtubeLink }),
      });
      const data = await response.json();
      setRecipe(data.recipe);
    } catch (error) {
      console.error('Error fetching recipe:', error);
      setRecipe('Error fetching recipe. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>Recipe Extractor</h1>
      <SearchBar onSubmit={fetchRecipe} />
      {recipe && <RecipeDisplay recipe={recipe} />}
    </div>
  );
}

export default App;