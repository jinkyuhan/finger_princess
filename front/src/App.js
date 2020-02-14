import React from 'react';
import { HashrRouter, Route } from 'react-router-dom';
import Wellcome from './routes/Wellcome';
import Questions from './routes/Questions'

function App() {
  return (
    <HashRouter>
      <Route path='/' exact={ true } component={ Wellcome } />
      <Route path='/questions' exact={ true } component={ Questions } />
    </HashRouter>
  )
}