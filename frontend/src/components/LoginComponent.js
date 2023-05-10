import React from "react";
import { CognitoUser, AuthenticationDetails } from 'amazon-cognito-identity-js'
import UserPool from '../components/aws-cognito/UserPool'
import { useState } from 'react'
import { useNavigate } from "react-router-dom";

export default function LoginComponent() {

  const [email, setEmail] = useState(null);
  const [password, setPassword] = useState(null);
  const navigate = useNavigate();

  const handleLogin = (e) => {
    console.log(process.env.REACT_APP_USER_POOL_ID);
    console.log(process.env.REACT_APP_USER_POOL_CLIENT_ID);
    e.preventDefault();

    const user = new CognitoUser({
      Username: email,
      Pool: UserPool
    });

    const authDetails = new AuthenticationDetails({
      Username: email,
      Password: password
    });

    user.authenticateUser(authDetails, {
      onSuccess: (data) => {
        console.log("success");
        navigate('/services');
      }, onFailure: (data) => {
        alert("Invalid credentials!!")
      }
    });
  }

  
  return (
    <section className="vh-100">
      <div className="container py-5 h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-12 col-md-8 col-lg-6 col-xl-5">
            <div
              className="card shadow-2-strong"
              style={{ borderRadius: "1rem" }}
            >
              <div className="card-body p-5 text-center">
                <h3 className="mb-5">Sign in</h3>

                <div className="form-outline mb-4">
                  <input
                    type="email"
                    id="typeEmailX-2"
                    className="form-control form-control-lg"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                  />
                  <label className="form-label" htmlFor="typeEmailX-2">
                    Email
                  </label>
                </div>

                <div className="form-outline mb-4">
                  <input
                    type="password"
                    id="typePasswordX-2"
                    className="form-control form-control-lg"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                  />
                  <label className="form-label" htmlFor="typePasswordX-2">
                    Password
                  </label>
                </div>

                {/* Checkbox */}
                <div className="form-check d-flex justify-content-start mb-4">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="form1Example3"
                  />
                  <label className="form-check-label" htmlFor="form1Example3">
                    {" "}
                    Remember password{" "}
                  </label>
                </div>

                <button
                  className="btn btn-primary btn-lg btn-block"
                  type="submit"
                  style={{ backgroundColor: "#4abdac" }}
                  onClick={(e) => handleLogin(e)}
                >
                  Login
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
