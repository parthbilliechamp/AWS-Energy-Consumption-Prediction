import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginPage from "../pages/LoginPage";
import Dashboard from "../pages/Dashboard";
import ViewPastRecordsPage from "../pages/ViewPastRecordsPage";
import ViewPrediction from "../pages/ViewPrediction";
import Services from "../pages/Services";
import AdminLoginPage from "../pages/AdminLoginPage";
import ServicesAdmin from "../pages/ServicesAdmin";
import TrainModelPage from "../pages/TrainModelPage";

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        /** User routes */
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/services" element={<Services />} />
        <Route path="/past_records" element={<ViewPastRecordsPage />} />
        <Route path="/prediction" element={<ViewPrediction />} />
        /** Admin routes */
        <Route path="/adminservices" element={<ServicesAdmin />} />
        <Route path="/admin" element={<AdminLoginPage />} />
        <Route path="/trainmodel" element={<TrainModelPage />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
