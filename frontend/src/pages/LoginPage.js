import React from "react";
import { Link } from "react-router-dom";
import LoginComponent from "../components/LoginComponent";

export default function LoginPage() {
  return (
    <div>
      <Link to="/admin">Login as Admin</Link>
      <LoginComponent />
    </div>
  );
}
