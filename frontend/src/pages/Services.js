import React from "react";
import ServiceCards from "../components/ServiceCard";
import Img1 from '../assets/images/Img1.jpg';
import Img2 from "../assets/images/Img2.jpg"

export default function Services() {
  const services = [
    {
      name: "View Past Energy Consumption records",
      image: Img1,
      link: "/past_records",
    },
    {
      name: "View Predictions for next 7 days",
      image: Img2,
      link: "/prediction",
    }
  ];

  return (
    <>
    <ServiceCards services={services} />
    </>
  )
}