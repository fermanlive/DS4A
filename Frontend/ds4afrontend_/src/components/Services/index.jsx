import React from 'react';
import Icon1 from '../../images/undraw_walking_around_25f5.png'
import IconArturo from '../../images/us/me.png'
import IconMartin from '../../images/us/martin.png'
import IconDaniel from '../../images/us/daniel.PNG'
import IconJuan from '../../images/us/juan.PNG'
import { ServicesContainer, ServicesWrapper, ServicesH1, ServicesH2, ServicesCard,ServicesP, ServicesIcon } from './ServicesElements'

const Services = () => {
  return (
    <ServicesContainer id='services'>
        <ServicesH1>Quienes somos</ServicesH1>
            <ServicesWrapper>
                <ServicesCard href = 'https://www.linkedin.com/in/ingarturorey/'>
                    <ServicesIcon src={IconArturo}/>
                    <ServicesH2>
                        Arturo Rey Haggar
                    </ServicesH2>
                    <ServicesP>
                        Ingeniero Mecanico / BI Developer
                    </ServicesP>
                </ServicesCard>
                <ServicesCard href = 'https://www.linkedin.com/in/daniel-fernando-murcia-perdomo/'>
                    <ServicesIcon src={IconDaniel}/>
                    <ServicesH2>
                        Daniel Murcia Perdomo
                    </ServicesH2>
                    <ServicesP>
                        Backend Machine Learning | Machine Learning Engineer in Progress
                    </ServicesP>
                </ServicesCard >
                <ServicesCard href = 'https://www.linkedin.com/in/marfelvasga'>
                    <ServicesIcon src={IconMartin}/>
                    <ServicesH2>
                        Martin Felipe Vasquez
                    </ServicesH2>
                    <ServicesP>
                        Ingeniero Mecanico | R&D Generative Design
                    </ServicesP>
                </ServicesCard>
                <ServicesCard href = 'https://www.linkedin.com/in/david-alexander-urrego-higuita-54675741/'>
                    <ServicesIcon src={Icon1}/>
                    <ServicesH2>
                        David Urrego
                    </ServicesH2>
                    <ServicesP>
                        Bioingeniero | Gestor CTeI
                    </ServicesP>
                </ServicesCard>
                <ServicesCard href = ''>
                    <ServicesIcon src={Icon1}/>
                    <ServicesH2>
                        Johanna Yama
                    </ServicesH2>
                    <ServicesP>
                        Ingeniera Agroindustrial
                    </ServicesP>
                </ServicesCard>
            
            </ServicesWrapper>
       
    </ServicesContainer>
  )
}

export default Services