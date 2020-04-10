'use strict';
const numOfBulbs = 10;

class Lights extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
      <ul id="lights">
        {Array(10).fill(1).map(() => {
          return <Bulb></Bulb>
        })}
      </ul>
    );
  }
}

const domContainer = document.querySelector('#christmas-lights');
ReactDOM.render(React.createElement(Lights), domContainer);