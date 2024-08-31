import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Alerts() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        const fetchAlerts = async () => {
            const response = await axios.get('http://localhost:5000/alerts/');
            setAlerts(response.data);
        };
        fetchAlerts();
    }, []);

    return (
        <div>
            <h2>Public Safety Alerts</h2>
            <ul>
                {alerts.map((alert) => (
                    <li key={alert.id}>
                        <strong>{alert.title}</strong> ({alert.level}) - {alert.description}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Alerts;
