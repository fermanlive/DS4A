import React, {useEffect, useState} from 'react';
import styled from 'styled-components';

const WrapperLoader = styled.div`
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: white;
    overflow: hidden;
    pointer-events: none;
    opacity: 0.95;
    display: flex;
    justify-content:center;
    align-items:center;
`
const Loader = styled.span`
    width: 48px;
    height: 48px;
    border: 5px solid #95BD62;
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: rotation 1s linear infinite;
    }

    @keyframes rotation {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }

`


const PageLoader = ({isLoading = false}) => {

    useEffect(() => {
        const root = document.querySelector('#root')
        root.style.pointerEvents =  isLoading ? "none": "auto";
    }, [isLoading])

    return isLoading ? (<WrapperLoader><Loader/></WrapperLoader>) : null;
}

export default PageLoader;