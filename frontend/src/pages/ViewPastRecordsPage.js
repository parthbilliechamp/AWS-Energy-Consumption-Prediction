import { React, useState } from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import HistoryPieChart from "../components/HistoryPieChart";
import HistoryLineGraph from "../components/HistoryLineGraph";
import HistoryBarGraph from "../components/HistoryBarGraph";
import "react-datepicker/dist/react-datepicker.css";
import DatePicker from "react-datepicker";
import { BASE_URL } from '../utils';


export default function ViewPastRecordsPage() {
  const [energyData, setEnergyData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());

  const handleOnClick = () => {
    const url = `${BASE_URL}/pastrecords?startDate=${startDate.toISOString()}&endDate=${endDate.toISOString()}`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setEnergyData(data);
        setIsLoading(false);
      });
  };

  return (
    <>
      <div className="container" style={{ marginBottom: "20px" }}>
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
              onClick={handleOnClick}
            >
              Generate Report
            </Button>
          </div>
        </div>
        <hr />
      </div>
      <Container>
        <br />
        <Row className="justify-content-center">
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <>
              <Row className="justify-content-center mb-8">
                <Col md={6}>
                  <h3 className="text-center">Bar Graph Visualization</h3>
                  <HistoryBarGraph energyData={energyData.bar_graph_data} />
                </Col>
              </Row>

              <Row className="justify-content-center">
                <Col md={6}>
                  <h3 className="text-center">Line Graph Visualization</h3>
                  <HistoryLineGraph energyData={energyData.line_graph_data} />
                </Col>
              </Row>

              <Col md={4}>
                <br />
                <br />
                <br />
                <h3 className="text-center">Pie Chart Visualization</h3>
                <div className="d-flex justify-content-center">
                  <HistoryPieChart energyData={energyData.pie_chart_data} />
                </div>
              </Col>
              <Row className="justify-content-center">
                <Col md={6} className="text-center">
                  <Button
                    variant="primary"
                    className="mt-4"
                    style={{ backgroundColor: "#4abdac" }}
                  >
                    Download Report
                  </Button>
                  <br />
                  <br />
                </Col>
              </Row>
            </>
          )}
        </Row>
      </Container>
    </>
  );
}
