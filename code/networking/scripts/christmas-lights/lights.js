
var lights = {
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

  return React.createElement(
    'ul',
    { style: lights },
    Array(50).fill(1).map(function (x, i) {
      return React.createElement(Bulb, { key: i, index: i });
    })
  );
}

ReactDOM.render(React.createElement(Lights, null), document.getElementById('christmas-lights'));