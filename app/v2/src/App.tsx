import React from "react";
import "./App.css";
// import Info from './assets/svg/info.svg';
import ParkingInfo from './components/ParkingInfo'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ParkingInfo/>
      </header>
    </div>
  );
}

export default App;
