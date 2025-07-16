import React, { useState } from 'react';
import axios from 'axios';

const YellForm = () => {
    const [whoYelled, setWhoYelled] = useState('');
    const [reason, setReason] = useState('');
    const [count,setCount] = useState(1);
    const [status, setStatus] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try{
            await axios.post('http://127.0.0.1:8000/add-yell',
                {who_yelled: whoYelled,
                reason: reason,
                count:count,});
            setStatus('Your anger has been registered');
            setWhoYelled('');
            setReason('');
            setCount(1);
                } catch (error){
                    console.error(error);
                    setStatus('Error submitting yell.');
                }
        };
    

return (
    <div style={{ padding:'2rem' }}>
        <h2>Did you yell at Pranav?</h2>
        <form onSubmit={handleSubmit}>
            <input 
            type='text'
            placeholder="Who yelled?"
            value={whoYelled}
            onChange={(e) => setWhoYelled(e.target.value)}
            required
            />
            <br /><br />
            <input 
            type="text"
            placeholder="Reason"
            value={reason}
            onChange={(e) => setReason(e.target.value)}
            required
            />
            <br /><br />
        
            <br />
            <button type="submit">Submit</button>
        </form>
        {status && <p>{status}</p>}
    </div>
);
};

export default YellForm;