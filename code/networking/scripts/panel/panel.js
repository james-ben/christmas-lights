var panelStyles = {
    marginTop: '80px',
    backgroundColor: 'var(--var-color-text-light)',
    padding: '30px 100px',
    borderRadius: '3px'
}
var buttonContainer = {
    display: 'flex',
    justifyContent: 'space-between'
}
var button = {
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
// button:hover {
//     opacity: .9;
// }
// button[disabled]:hover {
//     opacity: .4;
//     cursor: auto;
// }
// button.submit {
//     opacity: 1;
//     cursor: pointer;
// }

const { useState } = React


function Panel() {
    const defaultProcedures = [{
        'id': Math.random().toString(36).substring(2, 15),
        'color_set': ['white'],
        'brightness': [0,1],
        'blink_time': [],
        'name': 'twinkle',
        'direction': '',
        'run_time': '10',
    },
    {
        'id': Math.random().toString(36).substring(2, 15),
        'color_set': ['blue'],
        'brightness': [0,1],
        'blink_time': [],
        'name': 'strobe',
        'direction': '',
        'run_time': '10',
    },
    {
        'id': Math.random().toString(36).substring(2, 15),
        'color_set': ['red'],
        'brightness': [0,1],
        'blink_time': [],
        'name': 'crazy',
        'direction': '',
        'run_time': '10',
    }
]
    const [procedures, setProcedures] = useState(defaultProcedures);

    let onSave = () => {
        console.log('Save')
    }
    let onRun = () => {
        runCustomProcedures(procedures)
    }
    let onOff = () => {
        runOff()
    }
    let saveButton = React.createElement('button', {style: button, onClick:onSave}, 'Save')
    let runButton = React.createElement('button', {style: button, onClick:onRun}, 'Run')
    let offButton = React.createElement('button', {style: button, onClick:onOff}, 'Off')

    return React.createElement(
        'div',
        { style: panelStyles },
        React.createElement('div', {style: buttonContainer},
            React.createElement('div', null, saveButton, runButton), offButton),
        React.createElement(ProcedureList, { procedures: procedures, setProcedureList: setProcedures }),
    );
}

ReactDOM.render(React.createElement(Panel, null), document.getElementById('panel'));