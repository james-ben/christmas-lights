const server = 'http://localhost:5000/'
// const procedures = [];

window.onload = () => {
    createRowEl({}, [], '');
}


function createRunTimeEl(id) {
    const el = document.createElement('input');
    el.type = 'text';
    el.placeholder='Time(s)';
    el.classList.add('runTime');
    return el;
}

function createNameEl(id, name) {
    const el = document.createElement('input');
    el.type = 'list';
    el.placeholder = 'Name';
    el.classList.add('name');
    el.setAttribute('list', 'names');
    if (name) el.innerText = `${name}: `;
    return el;
}

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

function createDirectionEl() {
    const el = document.createElement('input');
    el.type = 'list';
    el.placeholder = `Direction`;
    el.classList.add('direction');
    el.setAttribute('list', 'directions');
    return el;
}

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

function getChildrenValues(el) {
    const values = [];
    Array.from(el.children).forEach(child => {
        if (child.value) values.push(child.value);
    });
    return values;
}

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
// Example POST method implementation:
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST',
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
        'Content-Type': 'text/plain'
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data)
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}

function getProcedures() {
    const procedures = [];
    const rows = window['procedures'].querySelectorAll('.row')
    rows.forEach(row => {
        procedures.push(getProcedure(row));
    });
    return procedures;
}

async function runCustomProcedures() {
    const procedures = getProcedures();
    postData(`${server}/run`, procedures)
    .then((procedures) => {
        console.log(procedures);
    })
    .catch((error) => {
        console.error(error);
    });
}  

function setProcedureName(buttonEl) {
    const allButtons = window['custom_procedure'].querySelectorAll('#name button');
    allButtons.forEach(button => {
        button.dataValue = undefined;
        button.classList.remove('selected');
    });
    buttonEl.dataValue = true;
    buttonEl.classList.add('selected');
}
