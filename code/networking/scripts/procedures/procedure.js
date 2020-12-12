var inputStyles = {
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

var rowStyles = {
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
};

var colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
var names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];
var directions = ['Forward', 'Backward', 'Bounce'];



// const availableProcedures = () => await runGetProcedures()

function Procedure({procedure, setProcedure}) {
    const { id } = procedure;

    function changeProcedure({ currentTarget }) {
        const newName = currentTarget.value.toLowerCase();
        procedure.name = newName;
        setProcedure(id, procedure);
    }
    function changeRunTime({ currentTarget }) {
        procedure.run_time = currentTarget.value;
        setProcedure(id, procedure);
    }
    
    return (
        <div id='procedure' style={rowStyles}>
            <input type='text' placeholder='Seconds' style={runTimeStyles} value={procedure.run_time} onChange={changeRunTime}></input>
            <select id='names' style={inputStyles} onChange={changeProcedure} value={procedure.name}>
            {names.map(name => 
                <option value={name}>{name}</option>
            )}
            </select>
        </div>
    )
}