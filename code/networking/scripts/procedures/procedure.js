const rangeStyles = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1,
    margin: '0px 5px',
    maxWidth: '35px'
};
const directionStyles = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    fontWeight: 100,
    flex: 1,
    margin: '0px 5px 0px 10px'
};
const sectionStyles = {
    display: 'flex',
    flexFlow: 'row wrap',
    marginLeft: '20px',
    alignItems: 'center'
};
const colorOrderLabelStyles = {
    width: '90px',
    paddingLeft: '10px'
};
const fadeLabelStyles = {
    width: '50px'
};
const colorOrderStyles = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'center',
    marginLeft: '10px'
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
    backgroundImage: 'url(../static/delete.png)',
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
    backgroundImage: 'url(../static/edit.png)',
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
    
    
    function changeColorOrder({ currentTarget }) {
        procedure.color_ordered = currentTarget.checked
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
    
    function changeBlinkTimeMax({ currentTarget }) {
        procedure.blink_time[1] = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    function changeBlinkTimeMin({ currentTarget }) {
        procedure.blink_time[0] = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    function changeDirection({ currentTarget }) {
        procedure.direction = currentTarget.value;
        setProcedure(id, procedure)
    }
    
    function changeFade({ currentTarget }) {
        procedure.fade = currentTarget.checked;
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
            <div style={colorOrderStyles}>
                <label style={colorOrderLabelStyles} for="orderedColor">Keep Color Order: </label>
                <input style={inputStyles} onChange={changeColorOrder} type="checkbox" id="orderedColor" name="orderedColor" disabled={!isEditing} defaultChecked={procedure.color_ordered} />
            </div>

            <div style={sectionStyles}>
                <p style={{margin: '0 0 0 10px'}}>Brightness: </p>
                <div style={{display: 'flex'}}>
                    {isEditing && <input style={rangeStyles} type='text' placeholder='Brightness Min' defaultValue={procedure.brightness[0]} onChange={changeBrightnessMin}/>}
                    {!isEditing && <p style={rangeStyles}>{procedure.brightness[0]}</p>}
                    {isEditing && <input style={rangeStyles} type='text' placeholder='Brightness Max' defaultValue={procedure.brightness[1]} onChange={changeBrightnessMax}/>}
                    {!isEditing && <p style={rangeStyles}>{procedure.brightness[1]}</p>}
                </div>
            </div>
            <div style={sectionStyles}>
                <p style={{margin: '0 0 0 10px'}}>Blink Time: </p>
                <div style={{display: 'flex'}}>
                    {isEditing && <input style={rangeStyles} type='text' placeholder='Blink Time Min' defaultValue={procedure.blink_time[0]} onChange={changeBlinkTimeMin}/>}
                    {!isEditing && <p style={rangeStyles}>{procedure.blink_time[0]}</p>}
                    {isEditing && <input style={rangeStyles} type='text' placeholder='BLink Time Max' defaultValue={procedure.blink_time[1]} onChange={changeBlinkTimeMax}/>}
                    {!isEditing && <p style={rangeStyles}>{procedure.blink_time[1]}</p>}
                </div>
            </div>
            <div>
            {isEditing &&  <select id='direction' style={inputStyles} onChange={changeDirection} defaultValue='forward'>
                <option value='forward'>Forward</option>
                <option value='backward'>Backward</option>
                <option value='bounce'>Bounce</option>
            </select>}
            {!isEditing && <p style={directionStyles}>{procedure.direction}</p>}
            </div>
            <div style={colorOrderStyles}>
                <label style={fadeLabelStyles} for="fade">Fade: </label>
                <input style={inputStyles} onChange={changeFade} type="checkbox" id="fade" name="fade" disabled={!isEditing} defaultChecked={procedure.fade} />
            </div>
        </div>
    )
}