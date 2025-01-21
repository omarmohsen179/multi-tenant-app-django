import React from 'react';
import Notifications from './components/Notifications';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Multi-tenant Application</h1>
      </header>
      <main>
        <Notifications />
      </main>
    </div>
  );
}

export default App;