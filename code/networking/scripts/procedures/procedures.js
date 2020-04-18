var procedures = {
    width: '100%',
    display: 'flex',
    flexFlow: 'column nowrap'
};

var proceduresDiv = {
    flex: 1,
    marginRight: '5px'
};
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

var row = {
    display: 'flex',
    flexFlow: 'row nowrap',
    alignItems: 'stretch',
    justifyContent: 'space-between',
    margin: '10px 0px'
};

function Procedures() {
    return React.createElement(
        'div',
        { style: procedures },
        React.createElement(
            'datalist',
            { id: 'colors' },
            React.createElement('option', { value: 'Red' }),
            React.createElement('option', { value: 'Green' }),
            React.createElement('option', { value: 'Blue' }),
            React.createElement('option', { value: 'Yellow' }),
            React.createElement('option', { value: 'White' }),
            React.createElement('option', { value: 'Off' })
        ),
        React.createElement(
            'datalist',
            { id: 'names' },
            React.createElement('option', { value: 'Twinkle' }),
            React.createElement('option', { value: 'Stripes' }),
            React.createElement('option', { value: 'Strobe' }),
            React.createElement('option', { value: 'Blink' }),
            React.createElement('option', { value: 'Columns' })
        ),
        React.createElement(
            'datalist',
            { id: 'directions' },
            React.createElement('option', { value: 'Forward' }),
            React.createElement('option', { value: 'Backward' }),
            React.createElement('option', { value: 'Bounce' })
        )
    );
}

ReactDOM.render(React.createElement(Procedures, null), document.getElementById('procedures-container'));