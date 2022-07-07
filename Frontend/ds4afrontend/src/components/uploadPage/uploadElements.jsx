import styled from 'styled-components';
import {Link as LinkS} from 'react-scroll';
import {Link as LinkR} from 'react-router-dom';
import {FaTimes} from 'react-icons/fa';

export const UploadContainer = styled.div`
    max-width: 1000px;
    margin: 50px auto;
    display: grid;
    place-items: center;
    padding: 0 50px;
    grid-gap: 40px;

    @media screen and (max-width: 768px){
        padding: 0 20px;
    };

`

export const UploadH1 = styled.h1`
    color: #95BD62;
    font-size: 56px;
    display: flex;
    margin: 0 auto;
    text-align: center;

    @media screen and (max-width: 768px) {
        font-size: 40px;
    }

    @media screen and (max-width: 480px) {
        font-size: 32px;
    }
`

export const UploadTable = styled.table`
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    
    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    th{
        font-size: 24px;
        }
    td{
     font-size: 18px;
         &:hover {
         }
            cursor: pointer; 
    }

    tr:nth-child(even) {
      background-color: #d1ffc2;
    }
`

export const UploadButton1 = styled.input`
    border-radius: 8px;
    padding: 10px 0;
    font-size: 16px;

`

export const UploadButton2 = styled.button`
    border-radius: 50px;
    background: #997c74;
    white-space: nowrap;
    padding: 10px 22px;
    color: #fff;
    font-size: 16px;
    outline: none;
    border: none;
    transition: all 0.2s ease-in-out;
    cursor:pointer;
    &:hover{
        transition: all 0.2s ease-in-out;
        background: #C8BCBC;
        color: #010606;
    }
`

export const UploadH4 = styled.h4`
    font-size: 20px;
    text-align: justify;
    margin-bottom: 15px;
    
`

export const CloseModalButton = styled.button`
    max-width: max-content;
    margin: auto;
    border-radius: 4px;
    padding: 4px 12px;
    background: #eb6400;
    color: white;
    border: none;
    cursor: pointer;
`

export const ModalTitle = styled.h2`
    color: #95BD62;
    font-size: 36px;
    text-align: center;
`

export const ModalSubtitle = styled.h2`
    font-family: "Roboto","Helvetica","Arial",sans-serif;
    font-weight: 400;
    line-height: 1.5;
    letter-spacing: 0.00938em;
    margin-bottom: 0.35em;
    color: rgba(0, 0, 0, 0.6);
    font-size: 12px;
`

export const CardsWrapper = styled.div`
    display: grid;
    grid-auto-flow: column;
    grid-gap: 40px;
`

export const MetricCard = styled.div`
    width: 300px;
    text-align: center;
    background-color: #fff;
    color: rgba(0, 0, 0, 0.87);
    -webkit-transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    border-radius: 4px;
    border: 1px solid rgba(0, 0, 0, 0.12);
    overflow: hidden;
    display: grid;
    grid-gap: 15px;
    padding: 20px;
    
    h3{
        margin: 0;
        font-family: "Roboto","Helvetica","Arial",sans-serif;
        font-weight: 400;
        font-size: 1rem;
        line-height: 1.5;
        letter-spacing: 0.00938em;
        margin-bottom: 0.35em;
        color: rgba(0, 0, 0, 0.6);
        font-size: 24px;
    }
    
    p{
        margin: 0;
        font-family: "Roboto","Helvetica","Arial",sans-serif;
        font-weight: 400;
        font-size: 1.5rem;
        line-height: 1.334;
        letter-spacing: 0em;
        color: #1976d2;
    }
`




