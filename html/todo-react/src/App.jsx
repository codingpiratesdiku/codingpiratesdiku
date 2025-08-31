import { useState } from 'react';
import './App.css';
import codingPirates from './assets/Coding-Pirate-Logo-512px.png';

function App() {
  const [todos, setTodos] = useState([
    'Tag til Coding Pirates',
    'Spise pizza!',
  ]);
  const [input, setInput] = useState('');

  const onSubmit = (ev) => {
    ev.preventDefault();
    setTodos([...todos, input]);
  };

  return (
    <>
      <img src={codingPirates}></img>
      <h1>Hvad skal jeg lave i dag?</h1>
      <div className="card">
        <form onSubmit={onSubmit}>
          <input
            placeholder="Hvad skal du lave i dag?"
            onChange={(event) => setInput(event.target.value)}></input>
          <button type="submit">Indsæt i listen</button>
        </form>
      </div>
      <h2>Det her skal jeg lave i dag:</h2>
      <ul>
        {todos.map((todo, index) => {
          return <li key={index}>{todo}</li>;
        })}
      </ul>
    </>
  );
}

export default App;
