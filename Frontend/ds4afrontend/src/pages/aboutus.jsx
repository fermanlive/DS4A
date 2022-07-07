import React, {useState} from 'react'
import Sidebar from '../components/Sidebar';
import Navbar from '../components/Navbar';

import Footer from '../components/Footer';
import AboutUsHero from '../components/AboutUsHero';
import Services from '../components/Services';


const AboutUs = () => {
  
  const [isOpen, setIsOpen] = useState(false)

  const toggle = () => {
      setIsOpen(!isOpen)
  }
  return (
    <>

        <Sidebar isOpen={isOpen} toggle={toggle}/>
        <Navbar toggle={toggle}/>
        <AboutUsHero />
        <Services/>
        <Footer/>
    </>
  )
}

export default AboutUs