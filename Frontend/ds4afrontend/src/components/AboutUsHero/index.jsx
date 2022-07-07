import React from 'react'
import { HeroBg, HeroContainer, HeroH1, HeroP } from './AboutUsHeroElements'

const AboutUsHero = () => {
  return (
    <HeroContainer>
        <HeroBg>
            <HeroH1>Acerca de Nosotros</HeroH1>
            <HeroP>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Velit voluptate beatae labore porro? Voluptas, debitis id corrupti, expedita itaque nobis quidem veritatis deserunt vitae voluptatibus, accusantium perferendis et facilis dicta.</HeroP>
        </HeroBg>
    </HeroContainer>
  )
}

export default AboutUsHero