import { useEffect } from "react";
import {ADMIN_BASE_URL } from '../utils';

export default function TrainModelPage() {
  useEffect(() => {
    const getUserUrl = `${ADMIN_BASE_URL}/trainmodel`;
    fetch(getUserUrl)
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
      });
  }, []);
}
