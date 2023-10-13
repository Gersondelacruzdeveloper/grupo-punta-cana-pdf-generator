import React, { useState } from 'react';

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleLogin = async () => {
    if (!formData.email || !formData.password) {
      setError('Please fill in all fields.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/api/login_user', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`, // Include the access token
        },
        body: JSON.stringify(formData),
      });

     console.log('access_token', localStorage.getItem('access_token'))

      if (response.ok) {
        console.log("respond was ok", response)
        const data = await response.json();
        // Update tokens if necessary
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        // Redirect the user to the dashboard or another page upon successful login
        window.location.href = '/dashboard'; // Example redirection
      } else {
        const errorData = await response.json();
        setError(errorData.message);
      }
    } catch (error) {
      setError('Network error occurred. Please try again.');
    }
  };


  return (
    <div>
      <h2>Login</h2>
      <form>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <button type="button" onClick={handleLogin}>Login</button>

        {error && <div className="error-message">{error}</div>}
      </form>
    </div>
  );
};

export default Login;
