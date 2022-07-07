import styled from 'styled-components';


export const FooterContainer = styled.footer`
    background-color: #0B5FFF;

`

export const FooterWrap = styled.div`
    padding: 48px 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    max-width: 1100px;
    margin: 0 auto;

`

export const FooterLinksContainer = styled.div`
    display: flex;
    justify-content: center;

    @media screen and (max-width: 820px) {
        padding-top: 32px;
    };
`

export const FooterLinksWrapper = styled.div`
    display: flex;

    @media screen and (max-width: 820px) {
        flex-direction: column;
    };
`

export const FooterLinkItems = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin: 16px;
    text-align: left;
    width: 160px;
    box-sizing: border-box;
    color: #fff;

    @media screen and (max-width: 420px) {
        margin: 0;
        padding: 10px;
        width: 100%;
    };
`

export const FooterLinkTitle = styled.h1`
    font-size: 14px;
    margin-bottom: 16px;
`

export const FooterLink = styled.a`
    text-align: none;
    margin-bottom: 0.5rem;
    font-size: 14px;
    color: #fff;

    &:hover {
        color: #01bf71;
        transition: 0.3s ease-out;
    }
`
export const Img = styled.img`
    width: 200%;
    margin: 0 10px 10px -800px;
    padding-right: 100;

    @media screen and (max-width: 786px) {
        width: 100%;
        margin: 0 0 10px 0;
        padding-right: 0;
    };
`

