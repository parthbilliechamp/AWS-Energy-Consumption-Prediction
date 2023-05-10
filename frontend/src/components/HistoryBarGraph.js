import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "",
    },
  },
};

export default function HistoryBarGraph({ energyData }) {
  const labels = energyData.map((data) => data.DateAndTime);
  const data = {
    labels,
    datasets: [
      {
        label: "Sub Metering 1",
        data: energyData.map((data) => data.Sub_metering_1),
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      {
        label: "Sub Metering 2",
        data: energyData.map((data) => data.Sub_metering_2),
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      {
        label: "Sub Metering 3",
        data: energyData.map((data) => data.Sub_metering_3),
        backgroundColor: "rgba(53, 132, 245, 0.5)",
      },
    ],
  };

  return <Bar options={options} data={data} />;
}
