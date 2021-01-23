const panelStyles = {
    marginTop: '80px',
    backgroundColor: 'var(--var-color-text-light)',
    padding: '30px 100px',
    borderRadius: '3px'
}
const buttonContainerStyles = {
    display: 'flex',
    justifyContent: 'space-between'
}
const buttonStyles = {
    padding: '7px',
    borderRadius: '2px',
    boxShadow: 'none',
    fontSize: '.8rem',
    border: 'none',
    marginRight: '10px',
    cursor: 'pointer',
    background: 'var(--var-color-primary)',
    color: 'var(--var-color-text-light)',
    height: '35px',
    width: '70px',
    cursor: 'pointer',
}

const { useState } = React

function Panel() {
    const defaultProcedures = [
        {   'id': Math.random().toString(36).substring(2, 15),
            'color_set': ['#ffffff'],
            'brightness': [0,1],
            'blink_time': [.5, .5],
            'name': 'twinkle',
            'direction': 'forward',
            'run_time': '10',
            'color_ordered': true,
            'fade': false
        }
    ]
    const [procedures, setProcedures] = useState(defaultProcedures);

    const onSave = () => { console.log('Save') }
    const onRun = () => { runCustomProcedures(procedures) }
    const onOff = () => { runOff() }

    return (
        <div style={panelStyles}>
            <div style={buttonContainerStyles}>
                <div>
                    <button style={buttonStyles} onClick={onSave}>Save</button>
                    <button style={buttonStyles} onClick={onRun}>Run</button>
                </div>
                <button style={buttonStyles} onClick={onOff}>Off</button>
            </div>
            <ProcedureList procedures={procedures} setProcedureList={setProcedures}></ProcedureList>
        </div>
    )
}

ReactDOM.render(React.createElement(Panel, null), document.getElementById('panel'));