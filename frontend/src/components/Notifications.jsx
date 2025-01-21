import React, { useEffect, useState } from 'react';
import { HubConnectionBuilder } from '@microsoft/signalr';

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);
    const [connection, setConnection] = useState(null);

    useEffect(() => {
        const newConnection = new HubConnectionBuilder()
            .withUrl('ws://localhost:8000/ws/notifications/')
            .withAutomaticReconnect()
            .build();

        setConnection(newConnection);
    }, []);

    useEffect(() => {
        if (connection) {
            connection.start()
                .then(() => {
                    connection.on('notification', (message) => {
                        setNotifications(prev => [...prev, message]);
                    });
                })
                .catch(error => console.log('Connection failed: ', error));
        }
    }, [connection]);

    return (
        <div className="notifications">
            <h2>Notifications</h2>
            <div className="notification-list">
                {notifications.map((notification, index) => (
                    <div key={index} className="notification-item">
                        <h3>{notification.title}</h3>
                        <p>{notification.message}</p>
                        <small>{new Date(notification.created_at).toLocaleString()}</small>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Notifications; 