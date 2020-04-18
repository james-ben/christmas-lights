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

var runTime = {
    maxWidth: '75px'
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

};var colors = ['Red', 'Green', 'Blue', 'Yellow', 'White', 'Off'];
var names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];
var directions = ['Forward', 'Backward', 'Bounce'];

function getInputStyles(type) {
    return Object.assign({}, input, type);
}

function Procedure() {
    return React.createElement(
        'div',
        { id: 'procedure', style: row },
        React.createElement('input', { type: 'text', placeholder: 'Time(s)', style: getInputStyles(runTime) }),
        React.createElement('input', { type: 'list', placeholder: 'Name', style: getInputStyles(), list: names }),
        React.createElement('input', { type: 'list', placeholder: 'Direction', style: getInputStyles(direction), list: directions }),
        React.createElement(
            'div',
            { style: colorSet },
            React.createElement('input', { type: 'list', placeholder: 'Color', style: getInputStyles(), list: colors })
        ),
        React.createElement(
            'div',
            null,
            React.createElement('input', { type: 'text', placeholder: 'Min Brightness', style: getInputStyles() }),
            React.createElement('input', { type: 'text', placeholder: 'Max Brightness', style: getInputStyles() })
        ),
        React.createElement(
            'div',
            null,
            React.createElement('input', { type: 'text', placeholder: 'Min Blink Time', style: getInputStyles() }),
            React.createElement('input', { type: 'text', placeholder: 'Max Blink Time', style: getInputStyles() })
        )
    );
}