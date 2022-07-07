import React from 'react'
import { FooterContainer,FooterWrap,FooterLinksContainer,FooterLinksWrapper,FooterLinkItems,FooterLinkTitle,FooterLink,Img,Logo} from './FooterElements'
import MyImg from '../../images/footer.png'
const Footer = () => {
  return (
    <FooterContainer>
        
        <FooterWrap>
            <FooterLinksContainer>
                <FooterLinksWrapper>
                    <FooterLinkItems>
                        
                        <Img src={MyImg}/>
                    </FooterLinkItems>
                    
                </FooterLinksWrapper>
            </FooterLinksContainer>
        </FooterWrap>
    </FooterContainer>
  )
}

export default Footer

/* <FooterLinkTitle>About us</FooterLinkTitle>
<FooterLink href='https://arturorey.Medium.com'>Hello</FooterLink>
<FooterLink href='/signin'></FooterLink>
<FooterLink href='/signin'></FooterLink>
<FooterLink href='/signin'></FooterLink>
<FooterLink href='/signin'></FooterLink> */ 