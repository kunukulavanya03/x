import React, { useState } from 'react';
import '../pages/home.css';
import Hero from '../components/Hero'; 
import { login, register, logout } from './services/api';

const Home = () => {
  return (
    <div className="home-container">
      <Hero />

    </div>
  );
};

export default Home;