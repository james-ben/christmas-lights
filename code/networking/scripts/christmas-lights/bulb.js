
var bulb = {
  position: 'relative',
  display: 'inline-block',
  listStyle: 'none',
  margin: 0,
  padding: 0,
  width: 'var(--var-lights-width)',
  height: 'calc(var(--var-lights-width)*2)',
  borderRadius: '50%',
  animationFillMode: 'both',
  animationIterationCount: 'infinite',
  animationName: 'flash',
  animationDelay: '0s'
};

var casing = {
  display: 'block',
  width: 'var(--var-lights-width)',
  height: 'var(--var-lights-width)',
  background: '#2a2a2a',
  borderRadius: '3px'
};
var wire = {
  display: 'block',
  margin: 0,
  marginTop: '-30px',
  marginLeft: '7px',
  width: 'calc(var(--var-lights-width)*5)',
  height: 'calc(var(--var-lights-width))',
  borderRadius: '50%',
  borderBottom: '3px solid #2a2a2a'
};

var primary = {
  background: 'var(--var-color-primary-bright)',
  boxShadow: 'var(--var-color-primary-bright) 0px 0px 12px 5px'
};

var secondaryBright = {
  background: 'var(--var-color-secondary-bright)',
  boxShadow: 'var(--var-color-secondary-bright) 0px 0px 12px 5px'
};

var secondary = {
  background: 'var(--var-color-secondary)',
  boxShadow: 'var(--var-color-secondary) 0px 0px 12px 5px'
};

var accent = {
  background: 'var(--var-color-accent)',
  boxShadow: 'var(--var-color-accent) 0px 0px 12px 5px'
};

function generateStyleList(index) {
  var color = primary;
  if (index % 2 === 0) color = secondary;
  if (index % 3 === 0) color = secondaryBright;
  if (index % 4 === 0) color = accent;
  var speed = { animationDuration: (Math.random() + 1).toFixed(2) + 's' };
  var delay = { animationDelay: Math.random().toFixed(2) + 's' };
  return Object.assign({}, bulb, color, speed, delay);
}

function Bulb(_ref) {
  var index = _ref.index;

  var bulbStyleList = generateStyleList(index);
  return React.createElement(
    'span',
    null,
    React.createElement('div', { style: casing }),
    React.createElement('li', { style: bulbStyleList }),
    React.createElement('div', { style: wire })
  );
}