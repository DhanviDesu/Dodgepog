import React, {useState} from 'react';
import Button from '@material-ui/core/Button'
import './App.css';
import {ROOT_URL} from './constants'
function App() {
  const [response, setResponse] = useState(null);
  const ping = () => {
    fetch(ROOT_URL,{
      mode: 'cors'
    })
    .then(res => res.json())
    .then(
      data => {setResponse(JSON.stringify(data))}
    )
    .catch(() => {
      setResponse('oops ur fucked');
    })
  }


  return (
    <div className="App">
      <Button onClick={ping}>ping api endpoint</Button>
      { response
      ? <h1>{response}</h1>
      : <div/>
      }
    </div>
  );
}

export default App;
