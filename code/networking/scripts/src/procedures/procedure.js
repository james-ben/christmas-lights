const input = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    marginLeft: '5px',
    marginBottom: '5px',
    fontWeight: 100,
    flex: 1,
    width: '100%'
}

const runTime = {
    maxWidth: '75px'
}

const direction = {
    maxWidth: '100px'
}

const row = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'stretch',
    justifyContent: 'space-between',
    margin: '10px 0px',
    flex: 1,
    marginRight: '5px'
}

const colorSet = {
    display: 'flex',
    flexFlow: 'row wrap',
    padding: 0,
    margin: 0
}

const colorSetLabel = {
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
}
// .colorSet label:hover {
//     opacity: .9;
// }
// .colorSet input:checked + label {
//     opacity: 1;
// }

const colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
const names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];
const directions = ['Forward', 'Backward', 'Bounce'];

function getInputStyles(type) {
    return { ...input, ...type };
}

function Procedure() {
  return (
    <div id="procedure" style={row}>
        <input type='text' placeholder='Time(s)' style={getInputStyles(runTime)}></input>
        <input type='list' placeholder='Name' style={getInputStyles()} list={names}></input>
        <input type='list' placeholder='Direction' style={getInputStyles(direction)} list={directions}></input>
        <div style={colorSet}>
            <input type='list' placeholder='Color' style={getInputStyles()} list={colors}></input>
        </div>
        <div>
            <input type='text' placeholder='Min Brightness' style={getInputStyles()}></input>
            <input type='text' placeholder='Max Brightness' style={getInputStyles()}></input>
        </div>
        <div>
            <input type='text' placeholder='Min Blink Time' style={getInputStyles()}></input>
            <input type='text' placeholder='Max Blink Time' style={getInputStyles()}></input>
        </div>
    </div>
    )
}