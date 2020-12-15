const procedureListStyles = {
    width: '100%',
    display: 'flex',
    flexFlow: 'column nowrap'
}
const buttonStyles = {
    padding: '7px',
    borderRadius: '2px',
    boxShadow: 'none',
    fontSize: '.8rem',
    border: 'none',
    cursor: 'pointer',
    background: 'var(--var-color-primary)',
    color: 'var(--var-color-text-light)',
    height: '35px',
    width: '70px',
    cursor: 'pointer',
}

function ProcedureList({procedures, setProcedureList}) {
    const setProcedure = (id, newProcedure) => {
        const index = procedures.findIndex(procedure => procedure.id === id)
        procedures[index] = newProcedure;
        console.log(procedures)
        setProcedureList(procedures)
    }
    const createProcedureRow = () => {
        const newRow = {
            'id': Math.random().toString(36).substring(2, 15),
            'color_set': ['white'],
            'brightness': [0,1],
            'blink_time': [],
            'name': 'twinkle',
            'direction': '',
            'run_time': '10',
        }
        const newProcedures = procedures.concat(newRow)
        setProcedureList(newProcedures)
    }
    const removeProcedure = ({currentTarget}) => {
        const id = currentTarget.attributes.dataid.value
        const newProcedures = procedures.filter(p => p.id !== id)
        setProcedureList(newProcedures)
    }

    return (
        <div style={procedureListStyles}>
            {procedures.map(procedure =>
                <Procedure key={procedure.id} procedure={procedure} setProcedure={setProcedure} removeProcedure={removeProcedure}></Procedure>
            )}
            <button style={buttonStyles} onClick={createProcedureRow}>+</button>
        </div>
    )
}

// ReactDOM.render(React.createElement(ProcedureList, null), document.getElementById('procedures-container'));