const server = 'http://192.168.0.102:5000';

// POST method
async function postProcedure(command = '', data = {}) {
    const url = `${server}/${command}`;
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST',
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
        'Content-Type': 'text/plain',
      'Access-Control-Allow-Origin': '*'        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data)
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}

// GET method
async function getProcedures() {
    const url = `${server}/get/options`;
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'GET',
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        mode: 'no-cors',
        headers: {
        'Content-Type': 'text/plain',
      'Access-Control-Allow-Origin': '*' 
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}

// list options for get of get/options
// get/procedures
// get/colors
// get/presets
