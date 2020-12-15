const colorInputStyles = {
    border: 'none',
    width: '25px',
    height: '25px',
    padding: '0px',
    cursor: 'pointer'
  }
const editingColorInputStyles = {
  border: 'none',
  width: '25px',
  height: '25px',
  padding: '0px',
  background: '#fff',
  cursor: 'pointer'
}
const editingColorStyles = {
  width: '150px',
  display: 'flex',
  flexFlow: 'row wrap',
  background: '#fff',
  margin: '0px 5px',
  padding: '5px'
}
const colorStyles = {
  width: '150px',
  display: 'flex',
  flexFlow: 'row wrap',
  margin: '0px 5px',
  padding: '5px'
}
const colorContainerStyles = {
  display: 'flex',
  flexFlow: 'row wrap'
}

function ColorPicker({colors, setColors, isEditing}) {
    const changeColor = ({ currentTarget }) => {
      const newColor = currentTarget.value
      const colorIndex = currentTarget.attributes.key.value
      const newColors = colors
      newColors[colorIndex] = newColor
      setColors(newColors)
    };
    const addColor = () => {
      const newColors = [...colors, '#ffffff']
      setColors(newColors)
    }
    return (
      <div style={colorContainerStyles}>
          {isEditing && <div style={editingColorStyles}>
            {colors.map((color, index) => 
              <input type="color" style={editingColorInputStyles} defaultValue={color} onChange={changeColor} key={index}/>
            )}
          </div>}
          {!isEditing && <div style={colorStyles}>
            {colors.map((color, index) => 
              <input type="color" style={colorInputStyles} defaultValue={color} onChange={changeColor} key={index} disabled={!isEditing}/>
            )}
          </div>}
          <div>
            {isEditing && <button onClick={addColor}>+</button>}
          </div>
        </div>
    )
}