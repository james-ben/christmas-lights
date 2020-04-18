const procedures = {
    width: '100%',
    display: 'flex',
    flexFlow: 'column nowrap'
};

function createProcedureRow() {

}

function ProcedureList() {
  return (
    <div style={procedures}>
        <Procedure />
        <button>+</button>
    </div>
    )
}
 
ReactDOM.render(
  <ProcedureList />,
  document.getElementById('procedures-container')
);