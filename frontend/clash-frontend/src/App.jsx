import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function Button({ label, onClick}) {
	return (
		<button className="button" onClick={onClick}>
		  {label}
		</button>
	);
}

function MyComponent({ inputLabel = '', value, onChange }) {
  return (
    <div>
      {inputLabel && <label htmlFor="inputBox">{inputLabel}</label>}
      <input
	id={inputLabel}
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}


function App() {
  const [playertag, setPlayertag] = useState('')
  const [phone, setPhone] = useState('')
  const [password, setPassword] = useState('')
  const [otp, setOtp] = useState('')

  const handleSubmit = async () => {
	  const payload = {
		  playertag,
		  phone,
		  password,
		  otp
	  };

	  try {
		  const response = await fetch('http://localhost:8000/signup', {
			  method: 'POST',
			  headers: {
				  'Content-Type': 'application/json',
			  },
			  body: JSON.stringify(payload),
		  });

		  if (!response.ok) {
			  throw new Error('Failed to submit data');
		  }

		  const data = await response.json();
		  console.log('Success:', data);
		} catch (error) {
			console.error('Error:', error.message);
		}

  };

  return (
    <>
      <div className="SignupInfo">
	<p><MyComponent inputLabel="Player Tag" value={playertag} onChange={setPlayertag}/></p>
	<p><MyComponent inputLabel="Phone Number" value={phone} onChange={setPhone}/></p>
	<p><MyComponent inputLabel="Password" value={password} onChange={setPassword}/></p>
	<p><MyComponent inputLabel="API token" value={otp} onChange={setOtp}/></p>
      </div>
      <div>
	<Button label="Submit" onClick={handleSubmit} />
      </div>
    </>
  )
}

export default App
