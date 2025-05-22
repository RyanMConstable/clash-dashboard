import { useState } from 'react'
import './SignupPage.css'

function Button({ label, onClick}) {
	return (
		<button className="container-button" onClick={onClick}>
		  {label}
		</button>
	);
}

function MyComponent({ inputLabel = '', value, onChange, error, errorMessage }) {
  return (
    <div className="form-group">
      <input
	placeholder={inputLabel}
	id={inputLabel}
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
	className={`styled-input ${error ? 'input-error' : ''}`}
      />
      {error && <p className="input-error-text">{errorMessage}</p>}
    </div>
  );
}


function SignupPage() {
  const [playertag, setPlayertag] = useState('')
  const [phone, setPhone] = useState('')
  const [password, setPassword] = useState('')
  const [otp, setOtp] = useState('')

  const [errors, setErrors] = useState({ playertag: '', otp: '' });

  const handleSubmit = async () => {
	  const payload = {
		  "tag": playertag,
		  "phonenumber": phone,
		  "password": password,
		  "otp": otp
	  };

	  try {
		  const response = await fetch('/api/signup', {
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
		  console.log(data["status"]);

		  if (data.status === 'invalidplayertag') {
			  setErrors({ playertag: 'Invalid Player Tag', otp: '' });
		  } else if (data.status === 'invalidtoken') {
			  setErrors({ playertag: '', otp: 'Invalid Token' });
		  } else if (data.status === 'exists') {
			  setErrors({ playertag: 'Account already exists', otp: '' });
		  } else {
			  setErrors({ playertag: '', otp: '' });
		  }
	} catch (error) {
		console.error('Error:', error.message);
	}

  };

  return (
    <>
      <div className="InfoBox">
        <div className="SignupInfo">
	  <h2>Sign Up</h2>
	  <div><MyComponent inputLabel="Player Tag" value={playertag} onChange={setPlayertag} error={!!errors.playertag} errorMessage={errors.playertag}/></div>
	  <div><MyComponent inputLabel="Phone Number" value={phone} onChange={setPhone}/></div>
	  <div><MyComponent inputLabel="Password" value={password} onChange={setPassword}/></div>
	  <div><MyComponent inputLabel="API token" value={otp} onChange={setOtp} error={!!errors.otp} errorMessage={errors.otp}/></div>
        </div>
        <div>
	  <Button label="Submit" onClick={handleSubmit} />
        </div>
      </div>
    </>
  )
}

export default SignupPage
