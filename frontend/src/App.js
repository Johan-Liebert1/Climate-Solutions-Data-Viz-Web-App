import './App.css';
import axios from 'axios'
import React, { useState } from 'react'

function App() {
    const [power, setPower] = useState('')
    const [reqPower, setReqPower] = useState('')

    const submitHandler = (e) => {
        e.preventDefault()
        setReqPower(power)
    }

    return (
        <div className="App">
            <form onSubmit = {submitHandler}>
                <input type='text' value = {power} onChange = {(e) => setPower(e.target.value)} />
                <button type = 'submit'>Click</button>
            </form>

            <img src = {`/${reqPower}`} style = {{height: '500px'}} />
        </div>
    );
}

export default App;
