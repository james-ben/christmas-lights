const inputStyles = {
    fontSize: '20px',
    border: 'none',
    padding: '3px 5px',
    paddingRight: '2px',
    margin: '0px',
    marginLeft: '5px',
    fontWeight: 100,
    flex: 1,
    maxWidth: '159px'
  };

const names = ['twinkle', 'stripes', 'strobe', 'blink', 'columns'];

function ProcedureName({name, setName}) {

    function changeName({ currentTarget }) {
        const newName = currentTarget.value.toLowerCase();
        setName(newName);
    }
    
    return (
      <select id='names' style={inputStyles} onChange={changeName} defaultValue={name}>
      {names.map(name => 
          <option value={name}>{name}</option>
      )}
      </select>
    )
}