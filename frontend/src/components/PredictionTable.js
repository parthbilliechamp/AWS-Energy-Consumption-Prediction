import React from "react";
import { Table } from "react-bootstrap";

export default function PredictionTable({ energyData }) {
  return (
    <Table striped bordered hover style={{ width: "50%", marginTop: "60px" }}>
      <thead>
        <tr>
          <th>Date</th>
          <th>Predicted SM1</th>
          <th>Predicted SM2</th>
          <th>Predicted SM3</th>
        </tr>
      </thead>
      <tbody>
        {energyData.map((data) => (
          <tr key={data.DateAndTime}>
            <td>{data.DateAndTime}</td>
            <td>{data.Sub_metering_1}</td>
            <td>{data.Sub_metering_2}</td>
            <td>{data.Sub_metering_3}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
