const brightnessStyles = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1,
    maxWidth: '40px',
    margin: '0px 5px'
};
const editableRunTimeStyles = {
    maxWidth: '40px',
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1
};
const runTimeStyles = {
    maxWidth: '40px',
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1,
    margin: '0px'
};
const nameStyles = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1,
    margin: '0px',
    marginLeft: '10px',
    maxWidth: '120px'
};
const rowStyles = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'center',
    margin: '10px 0px',
    flex: '1',
    marginRight: '5px',
    backgroundColor: 'var(--var-color-text-light)'
};
const deleteButtonStyles = {
    padding: '7px',
    borderRadius: '2px',
    boxShadow: 'none',
    border: 'none',
    cursor: 'pointer',
    color: '#d11414',
    fontWeight: 'bold',
    backgroundImage: 'url(static/delete.png)',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'contain',
    backgroundColor: 'inherit',
    margin: '5px'
}
const editButtonStyles = {
    padding: '7px',
    borderRadius: '2px',
    boxShadow: 'none',
    border: 'none',
    cursor: 'pointer',
    backgroundImage: 'url(static/edit.png)',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'contain',
    backgroundColor: 'inherit',
    margin: '5px'
}

const colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
const directions = ['Forward', 'Backward', 'Bounce'];

// const availableProcedures = () => await runGetProcedures()

function Procedure({procedure, setProcedure, removeProcedure}) {
    const { id } = procedure
    const [isEditing, setIsEditing] = useState(false)
    function changeProcedureName(newName) {
        const newProcedure = Object.assign(procedure, {name: newName})
        setProcedure(id, newProcedure)
    }
    function changeRunTime({ currentTarget }) {
        procedure.run_time = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    function editProcedure() {
        setIsEditing(!isEditing)
    }
    
    function changeColors(newColors) {
        const newProcedure = Object.assign({}, procedure)
        newProcedure.color_set = newColors
        setProcedure(id, newProcedure)
    }
    
    function changeBrightnessMax({ currentTarget }) {
        procedure.brightness[1] = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    function changeBrightnessMin({ currentTarget }) {
        procedure.brightness[0] = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    return (
        <div id='procedure' style={rowStyles}>
            <button onClick={editProcedure} style={editButtonStyles} ></button>
            <button onClick={removeProcedure} style={deleteButtonStyles} id={procedure.id}></button>

            {isEditing && <input type='text' placeholder='Seconds' style={editableRunTimeStyles} defaultValue={procedure.run_time} onChange={changeRunTime}></input>}
            {!isEditing && <p style={runTimeStyles}>{procedure.run_time}</p>}
            <p style={runTimeStyles}>(s)</p>

            {isEditing && <ProcedureName name={procedure.name} setName={changeProcedureName}></ProcedureName>}
            {!isEditing && <p style={nameStyles} >{procedure.name}</p>}

            <ColorPicker colors={procedure.color_set} setColors={changeColors} isEditing={isEditing}></ColorPicker>

            <p style={{marginLeft: '10px'}}>Brightness (0-1): </p>
            {isEditing && <input style={brightnessStyles} type='text' placeholder='Brightness Min' defaultValue={procedure.brightness[0]} onChange={changeBrightnessMin}/>}
            {!isEditing && <p style={brightnessStyles}>{procedure.brightness[0]}</p>}
            {isEditing && <input style={brightnessStyles} type='text' placeholder='Brightness Max' defaultValue={procedure.brightness[1]} onChange={changeBrightnessMax}/>}
            {!isEditing && <p style={brightnessStyles}>{procedure.brightness[1]}</p>}
            
        </div>
    )
}