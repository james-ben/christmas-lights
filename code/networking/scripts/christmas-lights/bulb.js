
const bulb = {
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

const casingStyle = {
  display: 'block',
  width: 'var(--var-lights-width)',
  height: 'var(--var-lights-width)',
  background: '#2a2a2a',
  borderRadius: '3px'
};
var wireStyle = {
  display: 'block',
  margin: 0,
  marginTop: '-30px',
  marginLeft: '7px',
  width: 'calc(var(--var-lights-width)*5)',
  height: 'calc(var(--var-lights-width))',
  borderRadius: '50%',
  borderBottom: '3px solid #2a2a2a'
};

const primary = {
  background: 'var(--var-color-primary-bright)',
  boxShadow: 'var(--var-color-primary-bright) 0px 0px 12px 5px'
};

const secondaryBright = {
  background: 'var(--var-color-secondary-bright)',
  boxShadow: 'var(--var-color-secondary-bright) 0px 0px 12px 5px'
};

const secondary = {
  background: 'var(--var-color-secondary)',
  boxShadow: 'var(--var-color-secondary) 0px 0px 12px 5px'
};

const accent = {
  background: 'var(--var-color-accent)',
  boxShadow: 'var(--var-color-accent) 0px 0px 12px 5px'
};

function generateStyleList(index) {
  const color = primary;
  if (index % 2 === 0) color = secondary;
  if (index % 3 === 0) color = secondaryBright;
  if (index % 4 === 0) color = accent;
  const speed = { animationDuration: (Math.random() + 1).toFixed(2) + 's' };
  const delay = { animationDelay: Math.random().toFixed(2) + 's' };
  return Object.assign({}, bulb, color, speed, delay);
}

function Bulb(_ref) {
  const index = _ref.index;
  const bulbStyleList = generateStyleList(index);
  return (
    <span>
      <div style={casingStyle}></div>
      <li style={bulbStyleList}></li>
      <div style={wireStyle}></div>
    </span>
  )
}