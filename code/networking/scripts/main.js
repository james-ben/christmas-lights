// const server = 'http://192.168.0.114:5000';
const server = 'http://192.168.0.102:5000';
async function submitForm() {
    const form = window['custom_procedure'];
    await runCustomProcedure({
        'color_set': Array.from(form.querySelectorAll('.colorSet input:checked')).map(input => input.value),
        'color_ordered': form.querySelector('#colorOrdered').checked,
        'brightness': [form.querySelector('#brightnessMin').value, form.querySelector('#brightnessMax').value],
        'run_time': form.querySelector('#runTime').value,
        'blink_time': [form.querySelector('#blinkTimeMin').value, form.querySelector('#blinkTimeMax').value],
        'name': Array.from(form.querySelectorAll('#name button')).filter(x=>x.dataValue)[0].value,
        'direction': form.querySelector('#direction').value,
        'num_runs': form.querySelector('#numRuns').value
    });
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
  

async function runCustomProcedure(data) {
    postData(`${server}/run`, data)
    .then((data) => {
        console.log(data);
    });
}  
 
async function runProcedure(action) {
    debugger
    let response = {};
    try {
    switch(action) {
        case 'twinkle-color': 
            response = await fetch(`${server}/run/twinkle/color`);
            break;
        case 'twinkle-white':
            response = await fetch(`${server}/run/twinkle/white`);
            break;
        case 'stripes-up':
            response = await fetch(`${server}/run/stripes/up_ordered`);
            break;
        case 'stripes-up-down':
            response = await fetch(`${server}/run/stripes/upDown_ordered`);
            break;
        case 'strobe':
            response = await fetch(`${server}/run/strobe/upDown_ordered`);
            break;
        default: 
            break;
    }
    }
    catch (error) {
        console.error(error);
    }
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
