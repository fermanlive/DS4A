import React from 'react';
import {FaBars} from 'react-icons/fa';
import {Nav,
        NavbarContainer,
        NavLogo,
        MobileIcon,
        NavMenu,
        NavItem,
        NavLinks,
        NavBtn,
        NavBtnLink,
        Logo,
        NavLogo1} from './NavbarElements'

import myImage from '../../images/urt_img.png';


const Navbar = ({ toggle }) => {
  return (
    <>
        <Nav>
            <NavbarContainer>
                <NavLogo1 to='/'>
                    <Logo src={myImage}/>
                </NavLogo1>
                <MobileIcon onClick={toggle}>
                    <FaBars/>
                </MobileIcon>
                    <NavMenu>
                        <NavItem>
                            <NavLinks to='/upload'>Cargar Documento</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='/aboutus'>Acerca de Nosotros</NavLinks>
                        </NavItem>
                        {/* <NavItem>
                            <NavLinks to='/ds4a'>DS4A Colombia</NavLinks>
                        </NavItem> */}
                    </NavMenu>
                    <NavBtn>
                        {/* <NavBtnLink to='/signin'>Ingresa</NavBtnLink> */}
                    </NavBtn>
            </NavbarContainer>
        </Nav>
    </>
  )
}

export default Navbar