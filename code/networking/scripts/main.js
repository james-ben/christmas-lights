window.onload = () => {
    createRowEl({}, [], '');
}

// Create an input tag for generating runTime
function createRunTimeEl(id) {
    const el = document.createElement('input');
    el.type = 'text';
    el.placeholder='Time(s)';
    el.classList.add('runTime');
    return el;
}

// Create an input tag for generating the name according to a list of names
function createNameEl(id, name) {
    const el = document.createElement('input');
    el.type = 'list';
    el.placeholder = 'Name';
    el.classList.add('name');
    el.setAttribute('list', 'names');
    if (name) el.innerText = `${name}: `;
    return el;
}

// Create a container of inputs for adding colors according to a list of colors
function createColorEl(colorSet) {
    const el = document.createElement('div');
    const color = document.createElement('input');
    el.classList.add('color-set');
    color.type = 'list';
    color.placeholder = `Color`; 
    color.setAttribute('list', 'colors');
    if (colorSet.length) el.innerText = colorSet.join(', ');
    el.appendChild(color);
    el.appendChild(color.cloneNode(true));
    return el;
}

// Create an input tag for generating the direction of the procedure
function createDirectionEl() {
    const el = document.createElement('input');
    el.type = 'list';
    el.placeholder = `Direction`;
    el.classList.add('direction');
    el.setAttribute('list', 'directions');
    return el;
}

// Create a container of inputs to designate the minimum and maximum values of a given name
function createMinMaxEl(name) {
    const el = document.createElement('div');
    const min = document.createElement('input');
    const max = document.createElement('input');
    const className = name.toLowerCase().replace(' ', '-');
    el.classList.add(`${className}`);
    min.type = 'text';
    max.type = 'text';
    min.placeholder = `Min ${name}`;
    max.placeholder = `Max ${name}`;
    el.appendChild(min);
    el.appendChild(max);
    return el;
}

// Create a contianer called a row that will create all the input lines
function createRowEl(procedure, colorSet, name) {
    const proceduresElement = window['procedures'];
    const row = document.createElement('div');
    const id = procedure && procedure.id || '';
    row.classList.add('row');
    row.appendChild(createRunTimeEl(id));
    row.appendChild(createNameEl(id, name));
    row.appendChild(createDirectionEl());
    row.appendChild(createColorEl(colorSet) );
    row.appendChild(createMinMaxEl('Brightness'));
    row.appendChild(createMinMaxEl('Blink Time'));
    proceduresElement.appendChild(row);
}

// Create a list of values from the children of an element
function getChildrenValues(el) {
    const values = [];
    Array.from(el.children).forEach(child => {
        if (child.value) values.push(child.value);
    });
    return values;
}

// Get the procedure that will be sent to the christmas tree lights
function getProcedure(row) {
    const [ runTime, name, direction, colors, brightness, blinkTime] = Array.from(row.children);
    const colorSet = getChildrenValues(colors);
    const brightnessSet = getChildrenValues(brightness);
    const blinkTimeSet = getChildrenValues(blinkTime);
    return {
        'id': Math.random().toString(36).substring(2, 15),
        'color_set': colorSet,
        'brightness': brightnessSet,
        'blink_time': blinkTimeSet,
        'name': name.value.toLowerCase(),
        'direction': direction.value.toLowerCase(),
        'run_time': runTime.value,
    };
}

// Get all the procedures to be sent to the christmas tree lights
function getProcedures() {
    const procedures = [];
    const rows = window['procedures'].querySelectorAll('.row')
    rows.forEach(row => {
        procedures.push(getProcedure(row));
    });
    return procedures;
}

// run the procedures
async function runCustomProcedures() {
    const procedures = getProcedures();
    postProcedure('run', procedures)
    .then((procedures) => {
        console.log(procedures);
    })
    .catch((error) => {
        console.error(error);
    });
}