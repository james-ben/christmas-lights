var input = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    marginLeft: '5px',
    marginBottom: '5px',
    fontWeight: 100,
    flex: 1,
    width: '100%'
};

var runTimeStyles = {
    maxWidth: '75px',
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    marginLeft: '5px',
    marginBottom: '5px',
    fontWeight: 100,
    flex: 1,
    width: '100%'
};

var direction = {
    maxWidth: '100px'
};

var row = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'stretch',
    justifyContent: 'space-between',
    margin: '10px 0px',
    flex: 1,
    marginRight: '5px'
};

var colorSet = {
    display: 'flex',
    flexFlow: 'row wrap',
    padding: 0,
    margin: 0
};

var colorSetLabel = {
    content: '',
    display: 'flex',
    flexFlow: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100px',
    height: '50px',
    cursor: 'pointer',
    opacity: .4,
    color: 'var(--var-color-text-light)',
    margin: '2px 10px',
    borderRadius: '2px'
    // .colorSet label:hover {
    //     opacity: .9;
    // }
    // .colorSet input:checked + label {
    //     opacity: 1;
    // }

};

var colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
var names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];
var directions = ['Forward', 'Backward', 'Bounce'];



// const availableProcedures = () => await runGetProcedures()

function Procedure({procedure, setProcedure}) {
    const { id } = procedure;
    const [name, setName] = useState(procedure.name);
    const [runTime, setRunTime] = useState(procedure.run_time);

    function changeProcedure({ currentTarget }) {
        const newName = currentTarget.value.toLowerCase();
        const newProcedure = {
            blink_time: [],
            brightness: [0, 1],
            color_set: ["white"],
            direction: "",
            id,
            name: newName,
            run_time: runTime
         };
        setName(newName);
        setProcedure(id, newProcedure);
    }
    function changeRunTime({ currentTarget }) {
        setRunTime(currentTarget.value);
        procedure.run_time = currentTarget.value;
        setProcedure(id, procedure);
    }
    
    return React.createElement(
        'div',
        { id: 'procedure', style: row },
        React.createElement('input', { type: 'text', placeholder: 'Seconds', style: runTimeStyles, value: runTime, onChange: changeRunTime }),
        React.createElement(
            'select',
            { id: 'names', style: input, onChange: changeProcedure, value: name },
            React.createElement('option', { value: 'twinkle' }, 'Twinkle'),
            React.createElement('option', { value: 'stripes' }, 'Stripes'),
            React.createElement('option', { value: 'strobe'}, 'Strobe'),
            React.createElement('option', { value: 'blink' }, 'Blink'),
            React.createElement('option', { value: 'crazy' }, 'Crazy')
        )
    );
}