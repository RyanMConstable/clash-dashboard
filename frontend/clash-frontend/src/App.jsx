import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function MyComponent({ inputLabel = '' } ) {
  const [text, setText] = useState('');

  const handleChange = (event) => {
      setText(event.target.value);
  };

  return (
    <div>
      {inputLabel && <label htmlFor="inputBox">{inputLabel}</label>}
      <input
	id="inputBox"
        type="text"
        value={text}
        onChange={handleChange}
      />
    </div>
  );
}

function App() {

  return (
    <>
      <div className="SignupInfo">
	<p><MyComponent inputLabel="Player Tag "/></p>
	<p><MyComponent inputLabel="Phone Number "/></p>
	<p><MyComponent inputLabel="Password "/></p>
      </div>
    </>
  )
}

export default App
