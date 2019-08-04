import React from 'react';
import { Button } from 'antd';
import 'antd/dist/antd.css';
import './App.css';
import Sidebar from './Components/Sidebar';
import Navbar from './Components/Navbar';

function App() {
  return (
    <div>
      <Navbar />
      <Sidebar />
    </div>
  );
}

export default App;
