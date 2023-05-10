import React from "react";
import { Pie } from "react-chartjs-2";
import { Tooltip, Legend, Chart } from "chart.js";
import { ArcElement } from 'chart.js';

Chart.register(Tooltip, Legend, ArcElement);

export default function HistoryBarGraph( {energyData} ) {

  const totalEnergy =
    energyData.sub_metering1 +
    energyData.sub_metering2 +
    energyData.sub_metering3;

  const percentageData = {
    sub_metering1: ((energyData.sub_metering1 / totalEnergy) * 100).toFixed(2),
    sub_metering2: ((energyData.sub_metering2 / totalEnergy) * 100).toFixed(2),
    sub_metering3: ((energyData.sub_metering3 / totalEnergy) * 100).toFixed(2),
  };

  const options = {
    aspectRatio: 1,
    plugins: {
      tooltip: {
        callbacks: {
          label: function (context) {
            const label = context.label || "";
            const value = context.parsed || 0;
            const percentage = percentageData[context.dataIndex];

            return `${label}: ${value} (${percentage}%)`;
          },
        },
      },
    },
  };

  const data = {
    labels: ["Sub-metering 1", "Sub-metering 2", "Sub-metering 3"],
    datasets: [
      {
        label: "Energy Usage by Sub-metering Segment",
        data: [
          energyData.Sub_metering_1,
          energyData.Sub_metering_2,
          energyData.Sub_metering_3,
        ],
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
        hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
        borderWidth: 1,
      },
    ],
  };

  return <Pie data={data} options={options}/>;
}
