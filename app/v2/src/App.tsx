import React from "react";
import "./App.css";
// import Info from './assets/svg/info.svg';
import ParkingInfo from "./components/ParkingInfo";

/*
function return_color_id(rate: number) {
  if (rate < 50) {
    return 0
  }
  else if (50 <= rate && rate < 80) {
    return 1
  }
  else if (rate >= 80) {
    return 2
  }
}
*/


function App() {
  return (
    <div className="App">
      <h1 className="font-mono text-left text-3xl m-20">
        駐車場情報見れるくん
      </h1>
      <header className="App-header">  
        <ParkingInfo rate={0} />
      </header>
    </div>
  );
}

export default App;
