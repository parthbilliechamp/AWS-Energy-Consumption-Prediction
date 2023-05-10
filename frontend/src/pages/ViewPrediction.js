import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import PredictionLineGraph from "../components/PredictionLineGraph";
import PredictionTable from "../components/PredictionTable";
import { useEffect, useState, React } from "react";
import { BASE_URL } from '../utils';

export default function ViewPrediction() {

  const [energyData, setEnergyData] = useState([]);
  useEffect(() => {
    const getUserUrl = `${BASE_URL}/prediction`
    fetch(getUserUrl)
      .then((response) => response.json())
      .then((data) => {
        setEnergyData(data);
      });
  }, []);

  return (
    <Tabs
      defaultActiveKey="table"
      id="justify-tab-example"
      className="mb-3"
      justify
    >
      <Tab eventKey="table" title="View Tabular Data">
        <div className="d-flex justify-content-center">
          <PredictionTable energyData={energyData} />
        </div>
      </Tab>
      <Tab eventKey="graph" title="View Graph">
        <div className="d-flex justify-content-center">
          <PredictionLineGraph energyData={energyData} />
        </div>
      </Tab>
    </Tabs>
  );
}
