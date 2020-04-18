
  const lights = {
    overflow: 'hidden',
    position: 'fixed',
    zIndex: 1,
    margin:'-13px 0 0 -10px',
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
    <ul style={lights}>
      {Array(30).fill(1).map((x, i) => {
        return <Bulb index={i}></Bulb>
      })}
    </ul>
  )
}
 
ReactDOM.render(
  <Lights />,
  document.getElementById('christmas-lights')
);