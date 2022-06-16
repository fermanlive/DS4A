import { faker } from '@faker-js/faker';
// @mui
import { useTheme } from '@mui/material/styles';
import { Grid, Container, Typography } from '@mui/material';
// components
import Page from '../components/Page';
import Iconify from '../components/Iconify';
// sections
import {
  AppTasks,
  AppNewsUpdate,
  AppSimpleList,
  AppCurrentVisits,
  AppWebsiteVisits,
  AppTrafficBySite,
  AppWidgetSummary,
  AppCurrentSubject,
  AppConversionRates,
} from '../sections/@dashboard/app';
import { withGoogleMap, GoogleMap, Marker } from "react-google-maps"


// ----------------------------------------------------------------------

export default function File() {
  const theme = useTheme();
  const MyMapComponent = (props) =>
  <GoogleMap
    defaultZoom={8}
    defaultCenter={{ lat: -34.397, lng: 150.644 }}
  >
    {props.isMarkerShown && <Marker position={{ lat: -34.397, lng: 150.644 }} />}
  </GoogleMap>

  return (
    <Page title="Dashboard">
      <Container maxWidth="xl">
        <Typography variant="h4" sx={{ mb: 5 }}>
          Sentencia numero 050453121001-201601697-01 Chigorodó 27 noviembre 2018
        </Typography>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={6}>
            <AppSimpleList
              title="Order features"
              list={[...Array(5)].map((_, index) => ({
                id: faker.datatype.uuid(),
                title: [
                  'Cundinamarca',
                  'Martin Felipe',
                  'ELN',
                  'Garzon',
                  'Aprobada',
                ][index],
                type: `order${index + 1}`,
                detail: [
                  'departamento',
                  'Juez',
                  'Grupo Armado',
                  'Municipio',
                  'Resultado',
                ][index],
              }))}
            />
          </Grid>
          <Grid item xs={12} md={6} lg={6}>
            <AppSimpleList
              title="Order features"
              list={[...Array(5)].map((_, index) => ({
                id: faker.datatype.uuid(),
                title: [
                  '12 de noviembre 2021',
                  'Jorge Doe',
                  'Lorem ipsum',
                  'Lorem ipsum',
                  'Lorem ipsum',
                ][index],
                type: `order${index + 1}`,
                detail: [
                  'Fecha Sentencia',
                  'Recusado',
                  'Lorem ipsum',
                  'Lorem ipsum',
                  'Lorem ipsum',
                ][index],
              }))}
            />
          </Grid>
        </Grid>
      </Container>
    </Page>
  );
}
