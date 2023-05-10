import React from "react";
import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

export default function HistoryLineGraph( {energyData} ) {

  console.log(energyData)

  Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
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

  const labels = energyData.map((data) => data.DateAndTime);

  const sm1_data = {
    labels,
    datasets: [
      {
        label: "Sub Metering 1",
        data: energyData.map((data) => data.Sub_metering_1),
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      {
        label: "Sub Metering 2",
        data: energyData.map((data) => data.Sub_metering_2),
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      {
        label: "Sub Metering 3",
        data: energyData.map((data) => data.Sub_metering_3),
        borderColor: "rgb(74, 189, 172)",
        backgroundColor: "rgba(74, 189, 172)",
      },
    ],
  };

  return (
    <div style={{marginTop: "60px" }}>
      <Line options={options} data={sm1_data} />
    </div>
  );
}
