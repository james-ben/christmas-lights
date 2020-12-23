const colorInputStyles = {
    border: 'none',
    width: '25px',
    height: '25px',
    padding: '0px',
    cursor: 'pointer',
    background: 'inherit'
  }
const colorStyles = {
  width: '150px',
  display: 'flex',
  flexFlow: 'row wrap',
  margin: '0px 5px',
  padding: '5px'
}
const editingColorStyles = {
  width: '150px',
  display: 'flex',
  flexFlow: 'row wrap',
  margin: '0px 5px',
  padding: '3px 5px',
  backgroundColor: '#fff'
}
const colorContainerStyles = {
  display: 'flex',
  flexFlow: 'row wrap'
}
const addColorStyles = {
  marginTop: '7px'
}

function ColorPicker({colors, setColors, isEditing}) {
    const changeColor = ({ currentTarget }) => {
      const newColor = currentTarget.value
      const colorIndex = currentTarget.attributes.index.value
      const newColors = colors
      newColors[colorIndex] = newColor
      setColors(newColors)
    };
    const addColor = () => {
      const newColors = [...colors, '#ffffff']
      setColors(newColors)
    }
    const getColorStyles = () => {
      if (isEditing) return editingColorStyles
      return colorStyles
    }
    return (
      <div style={colorContainerStyles}>
          <div style={getColorStyles()}>
            {colors.map((color, index) => 
              <input type="color" style={colorInputStyles} defaultValue={color} onChange={changeColor} key={index} index={index} disabled={!isEditing}/>
            )}
          </div>
          <div>
            {isEditing && <button onClick={addColor} style={addColorStyles}>+</button>}
          </div>
        </div>
    )
}