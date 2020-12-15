const inputStyles = {
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

const names = ['Twinkle', 'Stripes', 'Strobe', 'Blink', 'Columns'];

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