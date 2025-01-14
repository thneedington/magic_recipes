import React from 'react';

function RecipeDisplay({ recipe }) {
  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h2>Recipe:</h2>
      <pre style={{ textAlign: 'left', margin: '0 auto', maxWidth: '600px', whiteSpace: 'pre-wrap' }}>
        {recipe}
      </pre>
    </div>
  );
}

export default RecipeDisplay;