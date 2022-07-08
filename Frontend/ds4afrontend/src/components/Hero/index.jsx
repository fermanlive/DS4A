import React, {useState} from 'react'
import URT_Header from '../../images/pexels-rachel-claire-5531431.jpg';
import Video from '../../images/video_farm.mp4'
import {HeroContainer,
        HeroBg,
        VideoBg,
        ImageBg,
        HeroContent,
        HeroH1,
        HeroP,
        ArrowForward,
        ArrowRight,
        HeroBtnWrapper} from './HeroElements';
import {Button} from '../ButtonElement';
  
    
const HeroSection = () => {

  const [hover,setHover] = useState(false)

  const onHover = () => {
    setHover(!hover)
  }

  return (
    <HeroContainer id='home'>
        <HeroBg>
            <VideoBg autoPlay loop muted src={Video} type='video/mp4' />
            
        </HeroBg>
        <HeroContent>
          <HeroH1>Terretorno</HeroH1>
          <HeroP>
            Carga aqui documento tu y mira la sintesis de la sentencia deseada.
          </HeroP>
          <HeroBtnWrapper>
            <Button to='/upload' 
                    onMouseEnter={onHover} 
                    onMouseLeave={onHover}
                    primary='true'
                    dark='true'>
              Comencemos {hover ? <ArrowForward />: <ArrowRight />}
            </Button>
          </HeroBtnWrapper>
        </HeroContent>
    </HeroContainer>
  )
}

export default HeroSection

/*<ImageBg src={URT_Header} />*/