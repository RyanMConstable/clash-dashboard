import { useState } from 'react'
import './LoginPage.css'
import { useNavigate } from 'react-router-dom';

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


function LoginPage() {
  const [playertag, setPlayertag] = useState('')
  const [password, setPassword] = useState('')

  const [errors, setErrors] = useState({ playertag: '', password: '' });

  const navigate = useNavigate();

  const handleSubmit = async () => {
	  const payload = {
		  "user": playertag,
		  "password": password,
	  };

	  try {
		  const response = await fetch('/api/login', {
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

		  if (data.status === 'ok') {
			  const clantag = data.clantag;
			  navigate(`/clandashboard/${clantag}`);
		  } else {
			  setErrors({ playertag: '', password: 'Incorrect Login' });
		  }
	} catch (error) {
		console.error('Error:', error.message);
	}

  };

  return (
    <>
      <div className="InfoBox">
        <div className="LoginInfo">
	  <h2>Login</h2>
	  <div><MyComponent inputLabel="Player Tag" value={playertag} onChange={setPlayertag} error={!!errors.playertag} errorMessage={errors.playertag}/></div>
	  <div><MyComponent inputLabel="Password" value={password} onChange={setPassword}/></div>
        </div>
        <div>
	  <Button label="Submit" onClick={handleSubmit} />
        </div>
      </div>
    </>
  )
}

export default LoginPage
