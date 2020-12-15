const runTimeStyles = {
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

const rowStyles = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'stretch',
    justifyContent: 'space-between',
    margin: '10px 0px',
    flex: 1,
    marginRight: '5px'
};
const colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
const names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];
const directions = ['Forward', 'Backward', 'Bounce'];

// const availableProcedures = () => await runGetProcedures()

function Procedure({procedure, setProcedure}) {
    const { id } = procedure;

    function changeProcedureName(newName) {
        const newProcedure = Object.assign(procedure, {name: newName});
        setProcedure(id, newProcedure);
    }
    function changeRunTime({ currentTarget }) {
        procedure.run_time = currentTarget.value;
        setProcedure(id, procedure);
    }
    
    return (
        <div id='procedure' style={rowStyles}>
            <input type='text' placeholder='Seconds' style={runTimeStyles} defaultValue={procedure.run_time} onChange={changeRunTime}></input>
            <ProcedureName name={procedure.name} setName={changeProcedureName}></ProcedureName>
        </div>
    )
}