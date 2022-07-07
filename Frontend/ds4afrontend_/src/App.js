import './App.css';
//import {Nav,NavbarContainer,NavLogo} from './components/Navbar/NavbarElements';
import {BrowserRouter as Router, Route,Routes} from 'react-router-dom'
import Home from './pages';

import AboutUs from './pages/aboutus';
import Upload from "./pages/upload";


function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/aboutus' element={<AboutUs/>}/>
        <Route path='/upload' element={<Upload/>}/>
      </Routes>
    </Router>
  );
}

export default App;
