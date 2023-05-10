import { React, useState } from "react";
import "react-datepicker/dist/react-datepicker.css";
import DatePicker from "react-datepicker";
import { Button } from "react-bootstrap";

export default function DateRangeInput() {
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());

  return (
    <div className="container" style={{marginBottom: "20px"}}>
      <div className="row justify-content-center">
        <div className="col-md-4">
          <div className="form-group">
            <label htmlFor="start-date">Start Date</label>
            <DatePicker
              id="start-date"
              className="form-control"
              selected={startDate}
              onChange={(date) => setStartDate(date)}
              dateFormat="dd/MM/yyyy"
            />
          </div>
        </div>
        <div className="col-md-4">
          <div className="form-group">
            <label htmlFor="end-date">End Date</label>
            <DatePicker
              id="end-date"
              className="form-control"
              selected={endDate}
              onChange={(date) => setEndDate(date)}
              dateFormat="dd/MM/yyyy"
            />
          </div>
        </div>
        <div className="col-md-2">
          <Button
            variant="primary"
            className="mt-4"
            style={{ backgroundColor: "#4abdac" }}
          >
            Generate Report
          </Button>
        </div>
      </div>
      <hr/>
    </div>
  );
}
