import React from "react";
import ServiceCards from "../components/ServiceCard";
import Img1 from '../assets/images/Img1.jpg';

export default function ServicesAdmin() {
  const services = [
    {
      name: "Train the machine learning model",
      image: Img1,
      link: "/trainmodel",
    }
  ];

  return (
    <>
    <ServiceCards services={services} />
    </>
  )
}