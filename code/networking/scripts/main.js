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