import React, {useState} from 'react'
import Sidebar from '../components/Sidebar';
import Navbar from '../components/Navbar';

import Footer from '../components/Footer';
import {
    CardsWrapper,
    CloseModalButton, MetricCard, ModalSubtitle, ModalTitle,
    UploadButton1,
    UploadButton2,
    UploadContainer,
    UploadH1, UploadH4,
    UploadTable
} from "../components/uploadPage/uploadElements";
import PageLoader from "../components/PageLoader/PageLoader";
import Modal from 'react-modal';

const customModalStyles = {
    overlay: {
        zIndex: 20,
        justifyContent: 'center',
        alignItems: 'center',
        display: 'flex'
    },
    content: {
        maxWidth: '800px',
        maxHeight: '450px',
        position: 'auto',
        display: 'grid',
        gridGap: '20px'
    },
};


const Upload = () => {

    const [isOpen, setIsOpen] = useState(false)
    const [selectedFile, setSelectedFile] = useState();
    const [isFetching, setIsFetching] = useState(false);
    const [dataFetched, setDataFetched] = useState();

    const [modalIsOpen, setIsOpenModal] = useState(false);
    const [modalText, setModalText] = useState("");


    const toggle = () => {
        setIsOpen(!isOpen)
    }

    // On file select
    const onFileChange = (event) => {
        // Update the state
        setSelectedFile(event.target.files[0]);
    };

    // On file upload (click the upload button)
    const onFileUpload = async () => {
        // Create an object of formData
        setIsFetching(true);
        const formData = new FormData();

        // Update the formData object
        formData.append(
            "file",
            selectedFile,
            selectedFile.name
        );

        // Details of the uploaded file
        // Request made to the backend api
        // Send formData object
        const response = await fetch("http://127.0.0.1:8000/files/", {
            method: 'POST',
            body: formData,
        }).then(res => res.json());
        setIsFetching(false);
        setDataFetched(response)
        console.log(response)

    };

    const openModal = (text) => {
        setIsOpenModal(true);
        setModalText(text)
    };

    const closeModal = (text) => {
        setIsOpenModal(false);
    };

    const tableColVictimary = dataFetched ? Object.values(dataFetched['result_inference']['result_victimario']) : [];
    const tableColLost = dataFetched ? Object.values(dataFetched['result_inference']['result_perdida']) : [];
    const tableColRequest = dataFetched ? Object.values(dataFetched['result_inference']['result_solicitante']) : [];
    const tableColDesitions = dataFetched ? Object.values(dataFetched['result_inference']['result_decision']) : [];
    const tableColUbications = dataFetched ? Object.values(dataFetched['result_inference']['result_ubicacion']) : [];

    return (
        <>
            {/*//NOTE: POner el loader cuando se env[ia el archivo */}
            <PageLoader isLoading={isFetching}/>
            <Sidebar isOpen={isOpen} toggle={toggle}/>
            <Navbar toggle={toggle}/>
            <UploadContainer>
                <UploadH1> Cargar el archivo para extracción de Caracteristicas</UploadH1>

                <div>
                    <UploadH4>Subir el archivo de la sentencia a analizar, esperar la respuesta y despues dar click sobre cada uno de los respectivos porcentajes para obtener el fragmento de texto extraido que segun el modelo puede tener la caracteristica buscada.</UploadH4>
                    <UploadH4>Debido a la cuota de computo se recomieda descargar y usar sentencias con una cantidad de paginas inferior a 30 como los siguientes: <a target="_blank" href="https://drive.google.com/file/d/1e-UjApAeelixpTHRKH1c3ndyaeKbuM_4/view?usp=sharing">pdf</a></UploadH4>
                </div>
                <div>    
                    <UploadButton1 id="fileInput" type="file"  onChange={onFileChange}/>
                    <UploadButton2 onClick={onFileUpload}>Enviar</UploadButton2>
                </div>
                {dataFetched &&
                    <>
                        <UploadTable>
                            <thead>
                            <tr>
                                <th>Identificación del victimario</th>
                                <th>Tipología de la pérdida del bien</th>
                                <th>Solicitante</th>
                                {/*Va el numerito de probability*/}
                                {/*cuando se le da click al numerito aparece el modal con lo que está en sentenicia*/}
                                <th>Sentido de la decisión</th>
                                <th>Ubicación del predio</th>
                            </tr>
                            </thead>
                            <tbody>
                            {
                                Object.values(dataFetched['result_inference']['result_decision']).map((e, i) => {
                                    return (<>
                                        <tr>
                                            <td onClick={() => openModal(tableColVictimary[i].sentencia[0])}>{tableColVictimary[i].probability[0]}%</td>
                                            <td onClick={() => openModal(tableColLost[i].sentencia[0])}>{tableColLost[i].probability[0]}%</td>
                                            <td onClick={() => openModal(tableColRequest[i].sentencia[0])}>{tableColRequest[i].probability[0]}%</td>
                                            <td onClick={() => openModal(tableColDesitions[i].sentencia[0])}>{tableColDesitions[i].probability[0]}%</td>
                                            <td onClick={() => openModal(tableColUbications[i].sentencia[0])}>{tableColUbications[i].probability[0]}%</td>
                                        </tr>
                                    </>)
                                })
                            }

                            </tbody>
                        </UploadTable>
                        <CardsWrapper>
                            <MetricCard>
                                <h3>Tiempo de procesamiento: </h3>
                                <p> {dataFetched.metrics.time_processes_file} segundos</p>
                            </MetricCard>
                            <MetricCard>
                                <h3>Tiempo inferido: </h3>
                                <p> {dataFetched.metrics.inference_time} segundos</p>
                            </MetricCard>
                        </CardsWrapper>
                    </>
                }


                <Modal isOpen={modalIsOpen} contentLabel="Sentencia" shouldCloseOnEsc={false} style={customModalStyles}>
                    <ModalTitle>Fragmento de Texto</ModalTitle>
                    <ModalSubtitle>La siguiente es un fragmento de texto que podria contener la informacion requerida para obtención de la caracteristica deseada.</ModalSubtitle>
                    <hr/>
                    <p>{modalText}</p>
                    <CloseModalButton onClick={closeModal}>Cerrar</CloseModalButton>
                </Modal>

            </UploadContainer>
            <Footer/>
        </>
    )
}

export default Upload