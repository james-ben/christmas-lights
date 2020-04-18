var procedures = {
    width: '100%',
    display: 'flex',
    flexFlow: 'column nowrap'
};

function createProcedureRow() {}

function ProcedureList() {
    return React.createElement(
        'div',
        { style: procedures },
        React.createElement(Procedure, null),
        React.createElement(
            'button',
            null,
            '+'
        )
    );
}

ReactDOM.render(React.createElement(ProcedureList, null), document.getElementById('procedures-container'));