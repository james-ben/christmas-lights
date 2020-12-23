
const strandStyles = {
  overflow: 'hidden',
  position: 'fixed',
  zIndex: 1,
  margin: '-13px 0 0 -10px',
  padding: 0,
  display: 'flex',
  flexFlow: 'row',
  justifyContent: 'space-between',
  width: '100%',
  height: '7%',
  background: '#333'
};
function Lights() {
  return (
    <ul style={strandStyles}>
      {Array(50).fill(1).map( (x, i) => <Bulb key={i} index={i}></Bulb>)}
    </ul>
  )
}

ReactDOM.render(React.createElement(Lights, null), document.getElementById('christmas-lights'));