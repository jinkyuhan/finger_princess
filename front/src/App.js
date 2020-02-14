import React from 'react';
import { HashRouter, Route } from 'react-router-dom';
import Welcome from './routes/Welcome';
import Questions from './routes/Questions'
import Result from './routes/Result'
function App() {
  return (
    <HashRouter>
      <Route path='/' exact={ true } component={ Welcome }/>
      <Route path='/questions' exact={ true } component={ Questions } />
      <Route path='/result' exact= { true } component={ Result }/>
    </HashRouter>
  )
}

export default App;