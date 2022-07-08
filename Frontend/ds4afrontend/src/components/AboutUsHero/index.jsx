import React from 'react'
import { HeroBg, HeroContainer, HeroH1, HeroP } from './AboutUsHeroElements'

const AboutUsHero = () => {
  return (
    <HeroContainer>
        <HeroBg>
            <HeroH1>Acerca de Nosotros</HeroH1>
            <HeroP>Terretorno es un equipo multidisciplinario, multicultural de todas las regiones del país, abarcando desde la cálida costa Caribe, atravesando por la ciudad de la eterna primavera, cruzando por la fría y llena de oportunidades ciudad Capitalina, cubriendo al sur por la tierra de promisión y finalizando en la Ciudad Sorpresa de Colombia.
            {"\n"} Siendo nuestro punto más fuerte la multiculturalidad, optamos por restitución de tierras porque nos motiva la misión de esta institución y nos complementa con lo desafiante que es el proyecto de extracción de características en sentencias de restitución de tierras.
Los integrantes son:</HeroP>
        </HeroBg>
    </HeroContainer>
  )
}

export default AboutUsHero