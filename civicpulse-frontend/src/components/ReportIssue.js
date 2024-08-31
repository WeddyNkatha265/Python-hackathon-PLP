import React, { useState } from 'react';
import axios from 'axios';

function ReportIssue() {
    const [description, setDescription] = useState('');
    const [location, setLocation] = useState('');
    const [imageUrl, setImageUrl] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://localhost:5000/issues/', {
            description, location, image_url: imageUrl
        });
        setDescription('');
        setLocation('');
        setImageUrl('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Report an Issue</h2>
            <textarea placeholder="Describe the issue..." value={description} onChange={(e) => setDescription(e.target.value)} required />
            <input type="text" placeholder="Location" value={location} onChange={(e) => setLocation(e.target.value)} required />
            <input type="text" placeholder="Image URL" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} />
            <button type="submit">Submit</button>
        </form>
    );
}

export default ReportIssue;
